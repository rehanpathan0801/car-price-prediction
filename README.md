# 🚗 Car Price Predictor — Machine Learning Web App

An interactive **Machine Learning** web application that predicts the price of a car based on multiple parameters such as brand, year, mileage, fuel type, and more.  
Built using **Python**, **Streamlit**, and **Scikit-Learn**, this project combines data science with a user-friendly web interface.

---

## 🧭 Overview

This project demonstrates how machine learning can be applied to estimate the resale price of used cars using real-world data.  
Users can input key car details through an interactive web interface, and the trained regression model predicts the approximate market value.

---

## 🧮 Input Parameters

| Category | Example Values |
|-----------|----------------|
| Car Brand | Hyundai, Maruti, Toyota, etc. |
| Manufacturing Year | 2015, 2018, 2020 |
| Kilometers Driven | 45,000 km |
| Fuel Type | Petrol, Diesel, CNG |
| Seller Type | Dealer, Individual |
| Transmission Type | Manual, Automatic |
| Owner History | First Owner, Second Owner |
| Mileage | e.g., 18.2 km/l |
| Engine Capacity | e.g., 1197 cc |
| Maximum Power | e.g., 82 bhp |
| Number of Seats | e.g., 5 |

---

## 🧰 Tech Stack

- **Python 3.x**
- **Streamlit** – Frontend web app framework  
- **Pandas & NumPy** – Data manipulation  
- **Scikit-Learn** – Machine learning algorithms  
- **Matplotlib & Seaborn** – Data visualization (during model building)  

---

## 📁 Project Structure
```bash 
Car-Price-Predictor/
│
├── app.py # Main Streamlit app
├── model.pkl # Serialized trained ML model
├── CarDetails.csv # Dataset used for training
├── Car_Price_Model.ipynb # Jupyter notebook (model building & training)
├── requirements.txt # Project dependencies
└── README.md # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/Car-Price-Predictor.git
cd Car-Price-Predictor

```
### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Mac/Linux

```
---

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
---
### 🚀 Usage
```bash
streamlit run app.py
```
---
### 🧠 Model Details
The model is trained on car resale data and uses regression techniques to predict the price based on:

Brand

Manufacturing Year

Kilometers Driven

Fuel Type

Transmission

Seller Type

Owner History

Engine, Mileage, Power, and Seats

The preprocessing includes handling categorical data via Label Encoding and scaling numeric features for better accuracy.

---

### 📊 Example Output
```bash 
Car Price is going to be : ₹4,85,000
```
---

### 🎯 From data to decisions — predict your car’s true worth instantly!



