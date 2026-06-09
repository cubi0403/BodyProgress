# BodyProgress

BodyProgress 是一個健身與體態追蹤系統。

使用者可以：

* 新增身體測量資料
* 查看學員列表
* 搜尋學員
* 查看個人身體數據
* 產生進度圖表
* 下載 PDF 報告

## Tech Stack

* Python
* FastAPI
* Pandas
* Matplotlib
* ReportLab
* Jinja2
* Bootstrap 5

## Features

### Dashboard

顯示：

* 學員總數
* 測量紀錄總數

### Student Management

* 新增學員測量資料
* 搜尋學員
* 查看詳細資料

### Charts

* 體重變化
* 體脂變化
* 肌肉量變化
* 內臟脂肪變化

### PDF Reports

自動產生 PDF 進度報告。

## Run

```bash
pip install -r requirements.txt
uvicorn webapp.app:app --reload
```

Open:

http://127.0.0.1:8000
