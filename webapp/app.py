from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from fastapi import Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

import pandas as pd
import os
import subprocess
import sqlite3

app = FastAPI()

def get_db():

    conn = sqlite3.connect("bodyprogress.db")

    conn.row_factory = sqlite3.Row

    return conn

templates = Jinja2Templates(
    directory="webapp/templates"
)

@app.get("/")
def dashboard(request: Request):

    conn = get_db()

    student_count = conn.execute(
        """
        SELECT COUNT(DISTINCT name)
        FROM measurements
        """
    ).fetchone()[0]

    measurement_count = conn.execute(
        """
        SELECT COUNT(*)
        FROM measurements
        """
    ).fetchone()[0]

    conn.close()

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "student_count": student_count,
            "measurement_count": measurement_count
        }
    )

@app.get("/form", response_class=HTMLResponse)
def form_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


class Measurement(BaseModel):
    name: str
    date: str
    weight: float
    bodyfat: float
    muscle: float
    visceral_fat: float

@app.post("/add_measurement")
def add_measurement(data: Measurement):

    print("收到資料:", data)

    conn = get_db()

    conn.execute(
        """
        INSERT INTO measurements
        (name, date, weight, bodyfat, muscle, visceral_fat)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            data.name,
            data.date,
            data.weight,
            data.bodyfat,
            data.muscle,
            data.visceral_fat
        )
    )

    conn.commit()

    conn.close()

    return {
        "message": "success",
        "student": data.name
    }


@app.post("/generate_report/{student}")
def generate_report(student: str):

    try:

        subprocess.run(
            ["python", "chart.py"],
            check=True
        )

        subprocess.run(
            ["python", "pdf_report.py"],
            check=True
        )

        return {
            "status": "success",
            "student": student,
            "pdf": f"pdf_reports/{student}_Report.pdf"
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }


@app.get("/download_report/{student}")
def download_report(student: str):

    pdf_path = f"pdf_reports/{student}_Report.pdf"

    if os.path.exists(pdf_path):

        return FileResponse(
            pdf_path,
            media_type="application/pdf",
            filename=f"{student}_Report.pdf"
        )

    return {
        "error": "PDF not found"
    }

@app.post("/submit")
def submit_form(
        request: Request,
        name: str = Form(...),
        date: str = Form(...),
        weight: float = Form(...),
        bodyfat: float = Form(...),
        muscle: float = Form(...),
        visceral_fat: float = Form(...)
):
    conn = get_db()

    conn.execute(
        """
        INSERT INTO measurements
        (name, date, weight, bodyfat, muscle, visceral_fat)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            name,
            date,
            weight,
            bodyfat,
            muscle,
            visceral_fat
        )
    )

    conn.commit()

    conn.close()

    subprocess.run(
        ["python", "chart.py"],
        check=True
    )

    subprocess.run(
        ["python", "pdf_report.py"],
        check=True
    )

    return templates.TemplateResponse(
        request=request,
        name="success.html",
        context={
            "student": name
        }
    )

@app.get("/students")
def students_page(
    request: Request,
    search: str = ""
):

    conn = get_db()

    rows = conn.execute("""
        SELECT DISTINCT name
        FROM measurements
        ORDER BY name
    """).fetchall()

    students = [row["name"] for row in rows]

    conn.close()

    if search:

        students = [
            s for s in students
            if search.lower() in s.lower()
        ]

    return templates.TemplateResponse(
        request=request,
        name="students.html",
        context={
            "students": students,
            "search": search
        }
    )

@app.get("/student/{student}")
def student_page(
        request: Request,
        student: str
):

    conn = get_db()

    rows = conn.execute(
        """
        SELECT *
        FROM measurements
        WHERE name = ?
        ORDER BY date
        """,
        (student,)
    ).fetchall()

    conn.close()

    latest = rows[-1]
    first = rows[0]

    weight_change = latest["weight"] - first["weight"]
    bodyfat_change = latest["bodyfat"] - first["bodyfat"]
    muscle_change = latest["muscle"] - first["muscle"]
    visceral_change = latest["visceral_fat"] - first["visceral_fat"]

    return templates.TemplateResponse(
        request=request,
        name="student.html",
        context={
            "weight_change": round(weight_change, 1),
            "bodyfat_change": round(bodyfat_change, 1),
            "muscle_change": round(muscle_change, 1),
            "visceral_change": round(visceral_change, 1),
            "student": student,
            "weight": latest["weight"],
            "bodyfat": latest["bodyfat"],
            "muscle": latest["muscle"],
            "visceral_fat": latest["visceral_fat"]
        }
    )

@app.get("/chart/{student}/{chart_type}")
def get_chart(
        student: str,
        chart_type: str
):

    file = f"charts/{student}_{chart_type}.png"

    return FileResponse(file)