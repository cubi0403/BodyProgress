import subprocess
import sys

print("=================================")
print("BodyProgress 自動執行系統")
print("=================================")

files = [
    "main.py",
    "chart.py",
    "report.py"
]

for file in files:

    print(f"\n執行中：{file}")

    result = subprocess.run(
        [sys.executable, file]
    )

    if result.returncode == 0:
        print(f"✓ 完成：{file}")
    else:
        print(f"✗ 發生錯誤：{file}")
        break

print("\n全部流程完成！")