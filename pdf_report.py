import os
import pandas as pd

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# 註冊中文字體
pdfmetrics.registerFont(
    TTFont(
        'MicrosoftJhengHei',
        r'C:\Windows\Fonts\msjh.ttc'
    )
)

df = pd.read_csv("students.csv")

os.makedirs("pdf_reports", exist_ok=True)

styles = getSampleStyleSheet()

styles["Title"].fontName = "MicrosoftJhengHei"
styles["BodyText"].fontName = "MicrosoftJhengHei"
styles["Heading2"].fontName = "MicrosoftJhengHei"

students = df["name"].unique()

for student in students:

    data = df[df["name"] == student]
    data = data.sort_values("date")

    first = data.iloc[0]
    latest = data.iloc[-1]

    pdf_file = f"pdf_reports/{student}_Report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    content = []

    content.append(
        Paragraph(f"學員報告：{student}", styles["Title"])
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"日期區間：{first['date']} ~ {latest['date']}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"體重變化：{latest['weight'] - first['weight']:.1f} kg",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"體脂變化：{latest['bodyfat'] - first['bodyfat']:.1f} %",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"肌肉量變化：{latest['muscle'] - first['muscle']:.1f} kg",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"內臟脂肪變化：{latest['visceral_fat'] - first['visceral_fat']:.1f}",
            styles["BodyText"]
        )
    )

    # 加入圖表

    chart_files = [
        f"charts/{student}_weight.png",
        f"charts/{student}_bodyfat.png",
        f"charts/{student}_muscle.png",
        f"charts/{student}_visceral_fat.png"
    ]

    for chart in chart_files:

        if os.path.exists(chart):
            content.append(PageBreak())

            chart_name = (
                os.path.basename(chart)
                .replace(".png", "")
            )

            content.append(
                Paragraph(
                    chart_name,
                    styles["Heading2"]
                )
            )

            content.append(
                Spacer(1, 12)
            )

            content.append(
                Image(
                    chart,
                    width=450,
                    height=280
                )
            )

    # 建立PDF
    doc.build(content)

    print(f"已建立：{pdf_file}")