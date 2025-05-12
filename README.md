# 🧠 Obesity Risk Analysis

**Duration:** Feb 2025 – May 2025  
**Institution:** California State Polytechnic University, Pomona  
**Contributors:** Gerardo Gutierrez, Brandan Ly  

---

## 📌 Overview

This project investigates the key behavioral and demographic risk factors associated with obesity using a dataset from the UCI Machine Learning Repository. The analysis explores the strength of associations using correlation analysis, relative risk estimation, and logistic regression modeling.

---

## 📊 Dataset

- **Source:** UCI Machine Learning Repository  
- **Region:** Mexico, Peru, Colombia  
- **Size:** 2,111 observations, 17 attributes  
- **Note:** 77% of data synthetically generated using SMOTE

---

## 🔬 Methods

### 🧹 Data Wrangling
- Cleaned and enriched dataset using `pandas`
- Renamed variables for clarity
- Derived BMI from weight/height
- Created binary target variable (Obese vs Not Obese)
- One-hot encoded categorical variables for ML

### 📈 Exploratory Data Analysis
- Generated correlation heatmaps
- Visualized relationships using stacked bar graphs
- Analyzed trends in:
  - Family history of overweight
  - High-calorie food intake
  - Calorie monitoring

### 📉 Statistical Analysis
- **Relative Risk (RR)**: Calculated for binary predictors
- **Logistic Regression**: Used `scikit-learn` to model the probability of obesity and identify strongest predictors

---

## 📌 Key Findings

- **Top Predictors of Obesity**:
  - Family history of overweight (RR ≈ 3.18)
  - Not monitoring calories (RR ≈ 1.94)
  - Frequent high-calorie food intake (RR ≈ 1.63)

- Individuals who monitored their calorie intake had significantly lower obesity rates (~90% were not obese).
- Family history and poor nutritional habits emerged as the most consistent risk factors.

## 📄 Deliverables

- [📘 Final Report (PDF)](./reports/Report.pdf): Includes full methodology, analysis, visuals, and results
- [🖥️ Slide Deck (PDF)](./reports/ObesityRisk_Slides.pdf): Summary presentation of key findings
- Jupyter Notebook: Contains all code for preprocessing, EDA, modeling, and visualizations
