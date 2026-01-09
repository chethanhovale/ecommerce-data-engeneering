# 🛒 Ecommerce Data Engineering Project

An end-to-end **Data Engineering pipeline** built using **PostgreSQL, Python, Pandas, and SQLAlchemy**.  
This project demonstrates industry-style **RAW → CLEAN → ANALYTICS** data modeling.

---

## 📌 Project Overview

This project ingests ecommerce order data from a CSV file and processes it through multiple data layers:

- **RAW Layer** – Raw ingestion
- **CLEAN Layer** – Data validation & filtering
- **ANALYTICS Layer** – Fact tables & views for reporting

---

## 🧱 Architecture
CSV
↓
RAW Schema (raw.ecommerce_orders_raw)
↓
CLEAN Schema (clean.ecommerce_orders_clean)
↓
ANALYTICS Schema
├── fact_orders
└── views (payment usage, revenue, city analysis)

---

## 🛠️ Tech Stack

- Python 3.13
- PostgreSQL 18
- Pandas
- SQLAlchemy
- psycopg2
- pgAdmin
- Git & GitHub

---

## 📂 Project Structure

---

## 🛠️ Tech Stack

- Python 3.13
- PostgreSQL 18
- Pandas
- SQLAlchemy
- psycopg2
- pgAdmin
- Git & GitHub

---

## 📂 Project Structure
ecommerce-data-engineering/
├── data/
│ └── ecommerce_orders.csv
├── scripts/
│ └── run_pipeline.py
├── sql/
│ ├── schemas.sql
│ └── views.sql
├── .env
├── .gitignore
└── README.md
## Environment Setup
Create a `.env` file in the project root:

DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ecommerce_dw

🚀 How to Run the Pipeline
cd scripts
python run_pipeline.py

Successful run output:
Pipeline started
CSV loaded
RAW layer loaded
CLEAN layer created
ANALYTICS layer created
Pipeline completed successfully

📊 Analytics Examples

Total revenue by city
Orders by payment method
Daily revenue trends
## Author
Chethan Hovale  
Email: your.email@example.com  
GitHub: [github.com/chethanhovale](https://github.com/chethanhovale)
