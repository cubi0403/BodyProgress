import os
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3


# 讀取資料
conn = sqlite3.connect("bodyprogress.db")

df = pd.read_sql_query(
    "SELECT * FROM measurements",
    conn
)

conn.close()


# 建立圖表資料夾
os.makedirs("charts", exist_ok=True)


# 要產生的圖表
metrics = {
    "weight": "Weight (kg)",
    "bodyfat": "Body Fat (%)",
    "muscle": "Muscle (kg)",
    "visceral_fat": "Visceral Fat"
}


# 找出所有學員
students = df["name"].unique()


for student in students:

    student_data = df[df["name"] == student]

    # 日期排序
    student_data = student_data.sort_values("date")

    for metric, ylabel in metrics.items():

        plt.figure(figsize=(8, 4))

        plt.plot(
            student_data["date"],
            student_data[metric],
            marker="o"
        )

        plt.title(f"{student} - {metric}")
        plt.xlabel("Date")
        plt.ylabel(ylabel)

        plt.grid(True)

        plt.tight_layout()

        filename = f"charts/{student}_{metric}.png"

        plt.savefig(filename)

        plt.close()

        print(f"已建立：{filename}")


print("\n全部圖表產生完成!!!")