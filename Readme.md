# 🧠 Student Mental Health & Burnout — EDA Project

A comprehensive Exploratory Data Analysis (EDA) of student mental health and burnout patterns across 150,000 student records.

---

## 📁 Project Structure

```
├── student_mental_health_burnout.csv   # Raw dataset
├── EDA_Script.py                       # Main EDA Python script
├── Student_Mental_Health_EDA_Report.docx  # Full analysis report (Word)
└── EDA_output/
    ├── Image_1.png   # Financial State Distribution (Bar Chart)
    ├── Image_2.png   # Avg Study Hours by Gender (Pie Chart)
    ├── Image_3.png   # Depression Score by Academic Year (Line Chart)
    └── Image_4.png   # Physical Activity by Academic Year (Pie Chart)
```

---

## 📊 Dataset Overview

| Property        | Value                          |
|----------------|-------------------------------|
| Total Records   | 150,000                        |
| Total Features  | 20                             |
| Missing Values  | None                           |
| Age Range       | 17 – 25 years                  |
| CGPA Range      | 4.0 – 10.0                     |
| Academic Years  | 1st, 2nd, 3rd, 4th             |
| Gender Groups   | Male, Female, Other (~33% each)|

### Features

- **Identity:** `student_id`, `age`, `gender`, `course`, `year`
- **Academics:** `daily_study_hours`, `attendance_percentage`, `cgpa`, `academic_pressure_score`
- **Mental Health:** `stress_level`, `anxiety_score`, `depression_score`, `burnout_level`
- **Lifestyle:** `daily_sleep_hours`, `screen_time_hours`, `physical_activity_hours`, `sleep_quality`
- **Environment:** `financial_stress_score`, `social_support_score`, `internet_quality`

---

## ⚙️ Requirements

```bash
pip install pandas numpy matplotlib seaborn
```

---

## 🚀 How to Run

```bash
python EDA_Script.py
```

> Make sure to update the file path inside the script to point to your local CSV location before running.

---

## 📈 Analysis Performed

### 1. Financial Stress Classification
Students were categorized based on `financial_stress_score`:

| Category | Score Range | Count   |
|----------|-------------|---------|
| Good     | ≤ 3         | 44,932  |
| Average  | 3 – 7       | 60,309  |
| Bad      | ≥ 7         | 44,759  |

### 2. Gender vs. Daily Study Hours
All three gender groups show nearly identical average study hours (~5.5 hrs/day), indicating no gender-based study bias.

### 3. Depression Score by Academic Year
Depression peaks in **3rd year (5.518)** and declines in 4th year (5.476), reflecting mid-program academic pressure.

### 4. Physical Activity by Academic Year
Physical activity is uniformly low (~1 hr/day) across all academic years — no year-based variation.

### 5. Top Students by CGPA

| Rank | Student ID | CGPA |
|------|-----------|------|
| 1st  | 100039    | 10.0 |
| 2nd  | 234931    | 10.0 |
| 3rd  | 215471    | 10.0 |

---

## 🔍 Key Findings

- **40.2%** of students fall in the *Average* financial stress category; ~30% each in Good and Bad.
- **Depression peaks at 3rd year** — interventions should be targeted at this stage.
- **Burnout and stress levels** are uniformly distributed (~33% Low / Medium / High each).
- **Gender has no significant impact** on daily study hours or academic performance.
- **Physical activity is consistently low** regardless of academic year (~1 hr/day).

---

## 📄 Report

A full Word document report (`Student_Mental_Health_EDA_Report.docx`) is included, containing all charts, data tables, findings, and recommendations.

---

## 📝 Notes

- Duplicate rows were removed before analysis using `df.drop_duplicates()`.
- The dataset had **zero missing values** across all 20 columns.
- All charts were saved at 300 DPI for high-quality output.
