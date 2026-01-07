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

