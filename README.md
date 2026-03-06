# 🚀 CODTECH Python Development Internship

This repository contains the completed technical tasks for the CODTECH Internship, focused on practical Python development, data analysis, automation, NLP, and machine learning.  
Each task demonstrates real-world implementation using industry‑relevant libraries and frameworks.

---

## 📌 Task Overview

| Task | Description | Technologies |
|------|-------------|--------------|
| **Task 1** | Weather Dashboard – API integration & interactive data visualization | Streamlit, OpenWeatherMap API, Pandas, Matplotlib, Seaborn |
| **Task 2** | Automated PDF Report Generation – KPI analysis & business reporting | Pandas, Matplotlib, ReportLab |
| **Task 3** | AI Business Chatbot – NLP with TF‑IDF and cosine similarity | Streamlit, spaCy, scikit‑learn, JSON |
| **Task 4** | Machine Learning Model Implementation – supervised classification | Pandas, scikit‑learn, Matplotlib, Jupyter |

---

## 🌦 Task 1: Weather Dashboard (API Integration & Data Visualization)

**File:** [`weather_dashboard.py`](weather_dashboard.py)

### Description
An interactive Streamlit dashboard that:
- Fetches real‑time weather data from the OpenWeatherMap API
- Displays current weather metrics (temperature, humidity, wind speed)
- Visualises a 5‑day forecast (temperature, humidity, wind speed, weather conditions)
- Includes rolling average smoothing for temperature trends

### Features
- Secure API key handling via `.env`
- Current weather snapshot
- 5‑day forecast visualisations (line plots, bar chart)
- Matplotlib/Seaborn charts with 2×2 layout
- Error handling for invalid city names or API issues

### Setup & Run
1. **Create a `.env` file** in the project root and add your API key:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```
   > Get a free API key from [OpenWeatherMap](https://openweathermap.org/api).

2. **Install dependencies** (see [Installation](#⚙️-installation) below).

3. **Run the Streamlit app:**
   ```bash
   streamlit run weather_dashboard.py
   ```

---

## 📊 Task 2: Automated PDF Report Generation

**File:** [`generate_superstore_report.py`](generate_superstore_report.py)

### Description
A Python script that:
- Reads sales data from `Superstore.csv`
- Calculates key performance indicators (total sales, profit, orders, top category/region)
- Generates a professional PDF report (`Superstore_Report.pdf`) with:
  - Executive summary (KPIs)
  - Sample data table
  - Sales‑by‑category bar chart
- Cleans up temporary image files automatically

### Features
- Automatic KPI aggregation
- Styled tables using ReportLab
- Embedded Matplotlib chart
- Timestamped report generation

### Setup & Run
1. Ensure `Superstore.csv` is in the same directory.
2. Install dependencies.
3. Run:
   ```bash
   python generate_superstore_report.py
   ```
4. The generated PDF `Superstore_Report.pdf` will appear in the current folder.

---

## 🤖 Task 3: AI Business Chatbot (NLP)

**File:** [`app.py`](app.py)

### Description
A professional business chatbot built with:
- Intent‑based responses stored in `intents.json`
- TF‑IDF vectorisation and cosine similarity for matching user input
- spaCy for text preprocessing (tokenisation, lemmatisation)
- Streamlit UI with chat bubbles, sidebar quick questions, and session state persistence

### Features
- Confidence threshold (rejects queries below 0.2)
- Random response selection for variety
- Sidebar buttons for example questions
- Reset chat functionality
- Custom HTML/CSS message styling

### Setup & Run
1. **Download the spaCy model** (if not already installed):
   ```bash
   python -m spacy download en_core_web_sm
   ```
2. Install dependencies.
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## 📈 Task 4: Machine Learning Model Implementation

**File:** [`app.ipynb`](app.ipynb)

### Description
A Jupyter notebook that implements a spam‑detection classifier using:
- SMS Spam Collection dataset (`spam.csv`)
- Text preprocessing with TF‑IDF
- Multinomial Naive Bayes classifier
- Train/test split, accuracy evaluation, confusion matrix

### Concepts Covered
- Data loading & cleaning
- Feature extraction (TF‑IDF)
- Model training & prediction
- Performance metrics (accuracy, precision, recall, F1‑score)
- Confusion matrix visualisation

### Setup & Run
1. Ensure `spam.csv` is in the same directory.
2. Install dependencies.
3. Launch Jupyter Notebook / JupyterLab:
   ```bash
   jupyter notebook app.ipynb
   ```
4. Run all cells to see the training results and test predictions.

---

## ⚙️ Installation

All tasks share common Python dependencies. To set up the environment:

### 1. Clone the repository
```bash
git clone https://github.com/your-username/codetech-python-internship.git
cd codetech-python-internship
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install required packages
```bash
pip install -r requirements.txt
```

### 4. Additional step for Task 3 (spaCy model)
```bash
python -m spacy download en_core_web_sm
```

### 5. Set up environment variables (Task 1 only)
Create a `.env` file in the project root with your OpenWeatherMap API key:
```
OPENWEATHER_API_KEY=your_api_key_here
```

---

## 📁 Project Structure

```
codetech-python-internship/
│
├── weather_dashboard.py          # Task 1 – Weather Dashboard
├── generate_superstore_report.py  # Task 2 – PDF Report Generator
├── app.py                          # Task 3 – AI Chatbot
├── app.ipynb                       # Task 4 – ML Notebook
├── intents.json                     # Chatbot intents (Task 3)
├── Superstore.csv                   # Sales data (Task 2)
├── spam.csv                         # SMS dataset (Task 4)
├── .env.example                     # Example environment variables
├── requirements.txt                 # All Python dependencies
└── README.md                        # This file
```

---

## 🎯 Skills Demonstrated

- ✅ **API Integration** – OpenWeatherMap, secure key storage
- ✅ **Data Visualisation** – Matplotlib, Seaborn, interactive Streamlit
- ✅ **Automation & Reporting** – PDF generation with ReportLab
- ✅ **Natural Language Processing** – TF‑IDF, cosine similarity, spaCy
- ✅ **Machine Learning** – Supervised classification with scikit‑learn
- ✅ **Web App Development** – Streamlit interfaces, session state
- ✅ **Best Practices** – Error handling, environment variables, clean code

---

## 📌 Conclusion

This repository showcases a comprehensive set of Python skills applied to real‑world tasks. Each project is self‑contained, well‑documented, and ready to run.  
Feel free to explore, modify, and adapt the code for your own learning or professional projects.

---

**Author:** Yash Dhadve  
**Internship:** CODTECH Python Development  
**Date:** March 2025