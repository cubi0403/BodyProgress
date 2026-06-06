# BodyProgress

BodyProgress is a fitness coaching data analysis tool built with Python.

It helps coaches track student body measurements, analyze progress, generate charts, and create PDF reports automatically.

## Features

- Add new student measurements
- Analyze body composition changes
- Generate progress charts
- Create text reports
- Export PDF reports
- One-click automation workflow

## Tracked Metrics

- Weight
- Body Fat
- Muscle Mass
- Visceral Fat
- Body Age
- Chest
- Stomach
- Waist
- Lower Abdomen
- Hip
- Left/Right Thigh
- Left/Right Calf
- Left/Right Arm

## Project Structure

```text
BodyProgress
├── add_measurement.py
├── main.py
├── chart.py
├── report.py
├── pdf_report.py
├── run_all.py
├── students.csv
├── charts/
├── reports/
└── pdf_reports/
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Add measurement:

```bash
python add_measurement.py
```

Run full workflow:

```bash
python run_all.py
```

Generate PDF reports:

```bash
python pdf_report.py
```

## Current Version

v0.4

## Future Roadmap

- PDF reports with embedded charts
- BMI calculation
- Waist-to-hip ratio analysis
- Web dashboard
- FastAPI backend
- React frontend

## License

MIT License
