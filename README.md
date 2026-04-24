# prototype_timelead
# Logistics Lead Time Prediction System

A simple Machine Learning-based web application to predict processing time and analyze bottlenecks in logistics operations.

---

## Project Overview

This project aims to assist logistics operations by:

* Predicting **Packing → Ready Supply time**
* Calculating **Total Lead Time**
* Identifying **bottlenecks**
* Providing **actionable recommendations**

The system is built using:

* Python
* Machine Learning (Linear Regression)
* Streamlit (for web interface)

---

## How It Works

User inputs:

* **Order → Warehouse time**
* **Warehouse → Packing time**

System will:

1. Predict **Packing → Ready Supply time**
2. Calculate **Total Lead Time**
3. Identify the **longest process (bottleneck)**
4. Generate **insight & recommendation**

---

## Example Output

```
Estimated Packing → Ready: 21.86 minutes
Estimated Total Lead Time: 52.86 minutes

Bottleneck: Packing → Ready

Recommendation:
Increase manpower or improve packing efficiency
```

---

## Project Links

* Google Colab (Model Development):
[https://colab.research.google.com/drive/1_mfVXUY5344DCEw6_FizPmGFud-59b3_?usp=sharing]

* Live Web App (Streamlit):
[https://prototypetimelead-2nzwtuxdmwcodmmwncmpq5.streamlit.app/]

---

## Run Locally (VSCode / Terminal)

### 1. Install Dependencies

```
pip install -r requirements.txt
```

### 2. Terminal Local

```
python -m streamlit run app.py
```

### 3. Run Streamlit App

```
streamlit run app.py
```
---

## Model Details

* Algorithm: Linear Regression
* Input Features:

  * process_1 (Order → Warehouse)
  * process_2 (Warehouse → Packing)
* Target:

  * process_3 (Packing → Ready Supply)

### Evaluation Metrics:

* MAE (Mean Absolute Error)
* R² Score

---

## 🎯 Key Features

* 📊 Real-time prediction
* ⚠️ Bottleneck detection
* 🧠 Insight generation
* 🚀 Actionable recommendations
