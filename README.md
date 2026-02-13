# 🚀 CODTECH Python Development Internship

This repository contains the completed technical tasks for the CODTECH Internship, focused on practical Python development, data analysis, automation, NLP, and machine learning.

Each task demonstrates real-world implementation using industry-relevant libraries and frameworks.

---

# 📌 Task Overview

## 🌦 Task 1: Weather Dashboard (API Integration & Data Visualization)

📄 File: [`weather_dashboard.py`](sandbox:/mnt/data/weather_dashboard.py) 

### Description

A Streamlit-based interactive dashboard that:

* Fetches real-time weather data from the OpenWeatherMap API
* Displays current weather metrics
* Visualizes 5-day forecast trends using Matplotlib and Seaborn
* Includes rolling averages for temperature analysis

### Features

* Secure API key handling using `.env`
* Current weather snapshot
* 5-day forecast visualization
* Temperature trend with rolling average
* Humidity & wind speed analysis
* Weather condition frequency chart

### Technologies Used

* Python
* Streamlit
* OpenWeatherMap API
* Pandas
* Matplotlib
* Seaborn
* python-dotenv

## Setup Instructions
### Create Environment File
```bash
1. Create a new file named .env in the root directory of the project.
2. Open the .env.example file.
3. Copy all the variables from .env.example.
4. Paste them into your newly created .env file.
5. Replace the placeholder values with your actual credentials and API keys.
```

### Run the App
Install Dependencies
```bash
pip install -r requirements.txt
```

Start the Streamlit App 
```bash
streamlit run app.py
```

---

## 📊 Task 2: Automated PDF Report Generation

📄 File: [`generate_superstore_report.py`](sandbox:/mnt/data/generate_superstore_report.py) 

### Description

A Python automation script that:

* Reads sales data from a CSV file
* Performs KPI analysis
* Generates a professional business PDF report
* Embeds visualizations into the report

### Features

* Automatic KPI calculation (Sales, Profit, Orders)
* Category-level performance analysis
* Auto-generated bar chart
* Executive summary section
* Styled tables using ReportLab
* Clean temporary file handling

### Technologies Used

* Python
* Pandas
* Matplotlib
* ReportLab

### Run the Script

```bash
python generate_superstore_report.py
```

Output:

```
Superstore_Report.pdf
```

---

## 🤖 Task 3: AI Business Chatbot (NLP)

📄 File: [`app.py`](sandbox:/mnt/data/app.py) 

### Description

A professional business chatbot built using:

* TF-IDF vectorization
* Cosine similarity
* NLP preprocessing with spaCy
* Streamlit UI interface

### Features

* Intent-based response system
* TF-IDF text vectorization
* Cosine similarity scoring
* Confidence threshold handling
* Dynamic sidebar quick questions
* Chat history persistence using session state
* Custom chat bubble UI

### Technologies Used

* Python
* Streamlit
* spaCy
* scikit-learn
* JSON-based intent system


---

## 📈 Task 4: Machine Learning Model Implementation

📄 File: [`app.ipynb`](sandbox:/mnt/data/app.ipynb)

### Description

Implementation of a supervised machine learning model using scikit-learn for classification or prediction tasks.

### Concepts Covered

* Data preprocessing
* Feature selection
* Model training
* Model evaluation
* Prediction

### Technologies Used

* Python
* Pandas
* scikit-learn
* Matplotlib

---

# ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/codetech-python-internship.git
cd codetech-python-internship
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

If using spaCy:

```bash
python -m spacy download en_core_web_sm
```

3. Create a `.env` file (for Weather Dashboard):

```
OPENWEATHER_API_KEY=your_api_key_here
```

---

# 📁 Project Structure

```
codetech-python-internship/
│
├── weather_dashboard.py
├── generate_superstore_report.py
├── app.py
├── app.ipynb
├── intents.json
├── Superstore.csv
├── .env
└── README.md
```

---

# 🎯 Skills Demonstrated

* API Integration
* Data Visualization
* Automation & Reporting
* Natural Language Processing
* Machine Learning
* Streamlit App Development
* Secure Environment Variable Handling
* Business Data Analysis

---

# 📌 Conclusion

This repository reflects hands-on experience in building real-world Python applications involving backend logic, data analytics, automation, NLP systems, and predictive modeling.
