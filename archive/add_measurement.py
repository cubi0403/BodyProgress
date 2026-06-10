import csv
import os

filename = "student_detail.csv"

print("\n=== 新增學員量測資料 ===\n")

name = input("姓名：")
date = input("日期 (YYYY-MM-DD)：")

weight = input("體重(kg)：")
bodyfat = input("體脂(%)：")
muscle = input("肌肉量(kg)：")
visceral_fat = input("內臟脂肪：")
body_age = input("體年齡：")

print("\n--- 圍度資料 ---")

chest = input("胸圍(cm)：")
stomach = input("胃圍(cm)：")
waist = input("腰圍(cm)：")
lower_abdomen = input("小腹圍(cm)：")
hip = input("臀圍(cm)：")

left_thigh = input("左大腿圍(cm)：")
right_thigh = input("右大腿圍(cm)：")

left_calf = input("左小腿圍(cm)：")
right_calf = input("右小腿圍(cm)：")

left_arm = input("左手臂圍(cm)：")
right_arm = input("右手臂圍(cm)：")

new_row = [
    name,
    date,
    weight,
    bodyfat,
    muscle,
    visceral_fat,
    body_age,
    chest,
    stomach,
    waist,
    lower_abdomen,
    hip,
    left_thigh,
    right_thigh,
    left_calf,
    right_calf,
    left_arm,
    right_arm
]

with open(
    filename,
    "a",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)
    writer.writerow(new_row)

print("\n✅ 資料新增成功!!!")