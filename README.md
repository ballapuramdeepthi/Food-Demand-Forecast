Food Service Intelligence Platform

Empowering Restaurants with AI-Driven Demand Forecast

---

Project Overview

The Food Service Intelligence Platform is an AI-powered restaurant analytics solution designed to forecast menu demand, optimize inventory management, reduce food waste, and improve procurement planning. The platform leverages machine learning, predictive analytics, and business intelligence techniques to help restaurants make data-driven operational decisions.

Built using Python, Streamlit, XGBoost, SQLite, and Plotly, the application provides an interactive dashboard that combines demand forecasting, inventory monitoring, procurement recommendations, waste prediction, audit logging, and business analytics into a single intelligent platform.

---

Project Objective

The primary objective of this project is to develop an AI-driven decision support system that enables restaurants to:

- Forecast future menu demand accurately
- Optimize inventory utilization
- Reduce food wastage
- Improve procurement planning
- Monitor operational activities
- Support business decision-making
- Enhance restaurant profitability and efficiency

---

Key Features

Demand Forecasting

- XGBoost-based machine learning model
- Time-series demand prediction
- Future order forecasting
- Weather and festival demand adjustments
- Forecast history tracking

Inventory Management

- Inventory stock monitoring
- Reorder level management
- Low-stock alerts
- Inventory recommendations

Procurement Planning

- Smart procurement recommendations
- Required stock calculations
- Overstock and understock detection
- Purchase planning support

Waste Prediction

- Food wastage estimation
- Demand-based inventory optimization
- Waste reduction insights

Business Analytics

- Weekly demand analysis
- Rolling average demand trends
- Weekend demand comparison
- Seasonal demand insights
- Promotion effectiveness analysis

Audit Logging

- Inventory activity tracking
- Forecast generation logs
- Administrative activity monitoring

Reporting

- Forecast report generation
- Downloadable business reports
- Historical forecast records

Interactive Dashboard

- Streamlit-based web application
- Plotly visualizations
- Responsive user interface
- Light and Dark mode support

---

Technology Stack

Programming Language

- Python

Machine Learning

- XGBoost
- Scikit-Learn

Data Processing

- Pandas
- NumPy

Visualization

- Plotly

Database

- SQLite

Web Framework

- Streamlit

---

Machine Learning Workflow

Week 1: Data Collection and Exploratory Data Analysis

- Data collection and integration
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Demand trend analysis
- Cuisine popularity analysis
- Promotion impact analysis
- Pricing analysis

Week 2: Feature Engineering and Time-Series Preparation

- Date feature extraction
- Weekend feature creation
- Lag feature generation
- Rolling average calculations
- Categorical variable encoding
- Time-series dataset preparation

Week 3: Model Development and Evaluation

- XGBoost model training
- Model evaluation
- Forecast generation
- Model persistence using Joblib
- Streamlit deployment integration

---

Features Used for Forecasting

Calendar Features

- Year
- Month
- Day
- Day of Week
- Weekend Indicator

Lag Features

- Previous Demand (Lag-1)
- Previous Week Demand (Lag-7)

Rolling Statistics

- Rolling Mean Demand

Business Features

- Checkout Price
- Base Price
- Promotion Indicators
- Homepage Featured Status

Restaurant Features

- Meal ID
- Center ID
- City Code
- Region Code
- Operational Area

---

Project Structure

Food-Service-Intelligence-Platform/

├── app.py
├── requirements.txt
├── README.md
├── restaurant.db

├── data/
│   └── processed_data.csv

├── models/
│   └── xgboost_model.pkl

├── notebooks/
│   ├── Week1_EDA.ipynb
│   ├── Week2_Feature_Engineering.ipynb
│   └── Week3_Model_Training.ipynb

└── database/
    ├── db.py
    ├── schema.py
    └── audit_log.py

---
## 📸 Project Screenshots

### Dashboard
![Dashboard](outputs/Dashboard.png)

### Forecast
![Forecast](outputs/Forecast.png)

### Inventory
![Inventory](outputs/Inventory.png)

### Admin Dashboard
![Admin Dashboard](outputs/Admin_Dashboard.png)

### AI Chatbot
![AI Chatbot](outputs/AI Chatbot.png)
---
Database Tables

forecast_history

Stores all generated demand forecasts.

Column| Description
id| Forecast ID
meal_id| Meal Identifier
predicted_orders| Forecasted Demand
model_used| Machine Learning Model
forecast_date| Forecast Timestamp

inventory

Stores inventory information.

Column| Description
id| Inventory ID
ingredient| Ingredient Name
current_stock| Available Stock
reorder_level| Reorder Threshold
last_updated| Last Updated Timestamp

audit_logs

Stores system activities and logs.

Column| Description
id| Log ID
action| Activity Type
details| Activity Details
created_at| Timestamp

---

Installation Guide

Clone Repository

git clone <repository-url>

Install Dependencies

pip install -r requirements.txt

Create Database

python -m database.schema

Run Application

streamlit run app.py

---

Business Benefits

- Reduces food wastage
- Improves inventory utilization
- Enhances procurement planning
- Supports data-driven decisions
- Minimizes stock shortages
- Improves forecasting accuracy
- Increases operational efficiency
- Enhances restaurant profitability

---
Developed as an AI-Powered Restaurant Analytics and Decision Support System.