# 🚗 EV Analytics & Range Prediction System

## 📌 Project Overview

This project is an **end-to-end machine learning system** that analyzes electric vehicle (EV) data and predicts the **electric driving range** based on multiple real-world features.

It combines:

* 📊 Data Analysis (EDA)
* 🤖 Machine Learning (Model Comparison & Optimization)
* 🌐 Interactive Web App (Streamlit)

---

## 🎯 Objectives

* Analyze EV adoption trends and patterns
* Build a robust ML model to predict electric range
* Compare multiple models and select the best one
* Deploy a user-friendly interface for predictions

---

## 📊 Dataset

* Source: Kaggle (Electric Vehicle Population Dataset)
* Contains:

  * Manufacturer (Make)
  * Model Year
  * Electric Vehicle Type
  * County
  * CAFV Eligibility
  * Electric Range (Target Variable)

📥 **Note:** Dataset is not included due to size limits.
Download from Kaggle and place it in:

```
data/ev_data.csv
```

---

## 🧠 Machine Learning Pipeline

### ✔ Data Preprocessing

* Removed missing values and duplicates
* Filtered invalid entries
* Encoded categorical variables using LabelEncoder

---

### ✔ Feature Engineering

Used multiple real-world features:

* Make
* Model Year
* Electric Vehicle Type
* County
* CAFV Eligibility

---

### ✔ Model Comparison

Tested multiple algorithms:

* Linear Regression
* Decision Tree
* Random Forest

---

### ✔ Model Optimization

* Hyperparameter tuning using GridSearchCV
* Cross-validation for reliable performance

---

### ✔ Final Model

* Random Forest Regressor (optimized)

---

## 📈 Model Performance

* R² Score: **~0.98**
* Cross-validation score: (add your value)
* MAE: (add your value)

---

## 📊 Feature Importance

The model identifies key factors influencing EV range:

* Model Year
* Manufacturer
* Vehicle Type
* Location-based features

---

## 🌐 Streamlit Web App

### Features:

* User-friendly interface
* Dropdown-based input selection
* Real-time range prediction
* Safe encoding using saved encoders

---

## ⚙️ Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* Streamlit

---

## 🖥️ How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Add dataset

Place dataset in:

```
data/ev_data.csv
```

---

### 4. Run the app

```
python -m streamlit run app.py
```

---

## 📂 Project Structure

```
EV_Project/
│
├── data/                  # Dataset (not included)
├── model.ipynb            # ML pipeline
├── model.pkl              # Trained model
├── encoders.pkl           # Saved encoders
├── app.py                 # Streamlit UI
├── requirements.txt
└── README.md
```

---

## 🚀 Future Improvements

* Add more features (battery capacity, charging time)
* Improve model generalization
* Deploy on cloud (Streamlit Cloud / AWS)
* Add visual analytics dashboard

---

## ⚠️ Note on Model Accuracy

Although the model achieves high accuracy (~98%), cross-validation is used to ensure it is not due to overfitting or data leakage.

---

## 🙌 Conclusion

This project demonstrates a **complete machine learning workflow**, from data preprocessing to deployment, and provides insights into EV trends while delivering practical predictions.

---

## 📸 (Optional)

Add screenshots of your Streamlit app here for better presentation.

---
