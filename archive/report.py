import os
import pandas as pd

df = pd.read_csv("student_detail.csv")

os.makedirs("reports", exist_ok=True)

students = df["name"].unique()

for student in students:

    data = df[df["name"] == student]
    data = data.sort_values("date")

    first = data.iloc[0]
    latest = data.iloc[-1]

    weight_change = latest["weight"] - first["weight"]
    bodyfat_change = latest["bodyfat"] - first["bodyfat"]
    muscle_change = latest["muscle"] - first["muscle"]
    visceral_change = latest["visceral_fat"] - first["visceral_fat"]

    report = f"""
學員：{student}

日期區間：
{first['date']} ~ {latest['date']}

體重變化：
{weight_change:.1f} kg

體脂變化：
{bodyfat_change:.1f} %

肌肉量變化：
{muscle_change:.1f} kg

內臟脂肪變化：
{visceral_change:.1f}
"""

    filename = f"reports/{student}_report.txt"

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(report)

    print(f"已建立：{filename}")

print("\n全部報告產生完成!!!")