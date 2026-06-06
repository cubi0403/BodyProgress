import csv

students = {}

with open("students.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:

        name = row["name"]

        if name not in students:
            students[name] = []

        students[name].append(row)

for name, records in students.items():

    if len(records) < 2:
        print(f"{name} 資料不足")
        continue

    first = records[0]
    latest = records[-1]

    print("\n" + "=" * 40)
    print(f"學員：{name}")
    print("=" * 40)

    def show_change(label, field, unit=""):

        start = float(first[field])
        current = float(latest[field])

        diff = current - start

        if diff > 0:
            symbol = "增加"
        elif diff < 0:
            symbol = "減少"
        else:
            symbol = "無變化"

        print(
            f"{label}: "
            f"{start} → {current} "
            f"({symbol} {abs(diff)}{unit})"
        )

    show_change("體重", "weight", "kg")
    show_change("體脂", "bodyfat", "%")
    show_change("肌肉量", "muscle", "kg")
    show_change("內臟脂肪", "visceral_fat")
    show_change("體年齡", "body_age")

    show_change("胸圍", "chest", "cm")
    show_change("胃圍", "stomach", "cm")
    show_change("腰圍", "waist", "cm")
    show_change("小腹圍", "lower_abdomen", "cm")
    show_change("臀圍", "hip", "cm")

    show_change("左大腿", "left_thigh", "cm")
    show_change("右大腿", "right_thigh", "cm")

    show_change("左小腿", "left_calf", "cm")
    show_change("右小腿", "right_calf", "cm")

    show_change("左手臂", "left_arm", "cm")
    show_change("右手臂", "right_arm", "cm")

weight_change = (
    float(latest["weight"])
    - float(first["weight"])
)

bodyfat_change = (
    float(latest["bodyfat"])
    - float(first["bodyfat"])
)

muscle_change = (
    float(latest["muscle"])
    - float(first["muscle"])
)

waist_change = (
    float(latest["waist"])
    - float(first["waist"])
)

lower_abdomen_change = (
    float(latest["lower_abdomen"])
    - float(first["lower_abdomen"])
)

total_circumference_change = (
    (float(latest["chest"]) - float(first["chest"]))
    + (float(latest["stomach"]) - float(first["stomach"]))
    + (float(latest["waist"]) - float(first["waist"]))
    + (float(latest["lower_abdomen"]) - float(first["lower_abdomen"]))
    + (float(latest["hip"]) - float(first["hip"]))
    + (float(latest["left_thigh"]) - float(first["left_thigh"]))
    + (float(latest["right_thigh"]) - float(first["right_thigh"]))
    + (float(latest["left_calf"]) - float(first["left_calf"]))
    + (float(latest["right_calf"]) - float(first["right_calf"]))
    + (float(latest["left_arm"]) - float(first["left_arm"]))
    + (float(latest["right_arm"]) - float(first["right_arm"]))
)

visceral_change = (
    float(latest["visceral_fat"])
    - float(first["visceral_fat"])
)

print("\n綜合分析")
print("-" * 20)

if weight_change < 0:
    print(f"✓ 體重下降 {abs(weight_change)}kg")

if bodyfat_change < 0:
    print(f"✓ 體脂下降 {abs(bodyfat_change)}%")

if muscle_change > 0:
    print(f"✓ 肌肉量增加 {muscle_change}kg")

if visceral_change < 0:
    print(f"✓ 內臟脂肪下降 {abs(visceral_change)}")

if total_circumference_change < 0:
    print(
        f"✓ 總共減少 "
        f"{abs(total_circumference_change)}cm"
    )

print("\n評估：")

if (
    bodyfat_change < 0
    and muscle_change > 0
):
    print("你的效果太強啦!!!")
    print("脂肪下降而且肌肉量增加 oh my gosh")