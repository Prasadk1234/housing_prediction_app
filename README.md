# Housing Prediction App

A Django web application that predicts housing prices (Pune dataset) using pre-trained machine learning models and stores app data in SQLite. [attached_file:1]

## Overview
This project contains a Django project (`manage.py`, SQLite DB) and ML assets (notebook, CSV dataset, and `.pkl` model files) used for price prediction. [attached_file:1]

## Features
- House price prediction using pre-trained model files (`.pkl`). [attached_file:1]
- Django web app UI (inside `dashboard/` and `housing_prediction/`). [attached_file:1]
- Local development with SQLite (`db.sqlite3`). [attached_file:1]

## Tech Stack
- Backend: Django (Python). [attached_file:1]
- Database: SQLite (`db.sqlite3`). [attached_file:1]
- ML artifacts: Jupyter Notebook + Pickle models (`pune_price_model*.pkl`). [attached_file:1]

## Project Structure
```
housing_prediction_app/
├─ dashboard/                        # App (UI/views/templates)
├─ housing_prediction/               # Django project settings/urls/wsgi
├─ Pune house data.csv               # Dataset
├─ pune-housing-price-prediction.ipynb
├─ pune_price_model.pkl
├─ pune_price_model_lr.pkl
├─ pune_price_model_lr_model.pkl
├─ db.sqlite3
├─ manage.py
└─ requirements.txt
```
[attached_file:1]

## Getting Started (Local Setup)

### 1) Clone the repository
```bash
git clone https://github.com/Prasadk1234/housing_prediction_app.git
cd housing_prediction_app
```
[attached_file:1]

### 2) Create and activate a virtual environment (recommended)
**Windows (PowerShell)**
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
[attached_file:1]

### 4) Create environment variables (IMPORTANT)
Django projects commonly use environment variables for settings like `SECRET_KEY`, `DEBUG`, and allowed hosts. [web:34]

#### Option A: Using a `.env` file (recommended)
1. Create a file named `.env` in the project root (same folder as `manage.py`). [attached_file:1]
2. Add variables like:
```env
# Example values (update as needed)
DEBUG=True
SECRET_KEY=change-this-to-a-long-random-string
ALLOWED_HOSTS=127.0.0.1,localhost
python manage.py runserver
```
[web:34]

Open in browser:
- http://127.0.0.1:8000/ [web:34]

> Tip: The correct command format is `python manage.py runserver` (not `python runserver manage.py`). [web:34]

## Demo / Screenshots
A demo video is available in the project attachments (add it to the repo as `assets/demo.mp4` or upload to YouTube/Drive and link it here). [file:21]

## Notes
- This uses Django’s development server, which is intended for development/testing (not production). [web:34]
- Model files are included as `.pkl` in the repository. [attached_file:1]

## License
No license specified. [attached_file:1]

## Author
- GitHub: https://github.com/Prasadk1234 [attached_file:1]
