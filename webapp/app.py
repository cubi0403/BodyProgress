from fastapi import FastAPI
from fastapi.responses import FileResponse

from pydantic import BaseModel

import pandas as pd
import os
import subprocess

app = FastAPI()


@app.get("/")
def home():
    return {
        "project": "BodyProgress",
        "status": "running"
    }


class Measurement(BaseModel):
    name: str
    date: str
    weight: float
    bodyfat: float
    muscle: float
    visceral_fat: float


@app.post("/add_measurement")
def add_measurement(data: Measurement):

    file = "students.csv"

    new_row = pd.DataFrame([data.model_dump()])

    if os.path.exists(file):
        df = pd.read_csv(file)
        df = pd.concat([df, new_row], ignore_index=True)
    else:
        df = new_row

    df.to_csv(file, index=False)

    return {
        "message": "Measurement added successfully",
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