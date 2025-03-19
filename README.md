# 🚗 Car Insurance Claim Prediction

![Car Insurance Claim Prediction](https://via.placeholder.com/1200x400?text=Car+Insurance+Claim+Prediction)  
*A machine learning-based prediction model for insurance companies to assess the likelihood of a customer making an insurance claim.*

---

## 📌 Table of Contents
- [Overview](#overview)
- [Project Features](#project-features)
- [Dataset Description](#dataset-description)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [UI Screenshots](#ui-screenshots)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Model Performance](#model-performance)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 📖 Overview
This project predicts whether a customer will file a car insurance claim based on various parameters such as driving history, vehicle details, and past claims. The model helps insurance companies optimize risk assessment and reduce fraudulent claims.

---

## ✨ Project Features
✔️ Predicts the likelihood of an insurance claim  
✔️ Uses **Machine Learning (ML) algorithms** for prediction  
✔️ Web interface to input customer data  
✔️ Visualizes key insights from data  
✔️ REST API for integrating with other systems  

---

## 📂 Dataset Description
The dataset contains customer information including:
- **Demographics:** Age, gender, marital status, etc.
- **Vehicle Details:** Type, model year, previous claims
- **Policy Details:** Premium amount, coverage type
- **Driving History:** Past violations, accident history

---

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript (Flask-based UI)  
- **Backend:** Flask (Python)  
- **Machine Learning:** Scikit-Learn, XGBoost  
- **Database:** SQLite / PostgreSQL  
- **Visualization:** Matplotlib, Seaborn  

---

## 📂 Project Structure

car_insurance_claim_prediction/ │── app/ # Main application directory │ ├── static/ # CSS, JS, and images │ ├── templates/ # HTML templates for the UI │ ├── pycache/ # Cached Python files │ ├── app.py # Main Flask application │ ├── model.py # Machine Learning model training and prediction │ ├── preprocess.py # Data preprocessing script │── data/ # Dataset and preprocessing scripts │── .dockerignore # Docker ignore file │── .gitignore # Git ignore file │── Claim.png # UI Screenshot for Claim Output │── Home Page.png # UI Screenshot for Home Page │── No claim.png # UI Screenshot for No Claim Output │── Dockerfile # Dockerfile for containerization │── README.md # Project documentation │── car_insurance_pred.ipynb # Jupyter Notebook for EDA and model evaluation │── requirements.txt # Project dependencies 

---

## 📸 UI Screenshots
### 🔹 Homepage
![Homepage](Home%20Page.png)

### 🔹 No Claim Prediction Output
![No Claim](No%20claim.png)

### 🔹 Claim Prediction Output
![Claim](Claim.png)

---

## 🚀 Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/sruthy-sn91/car_insurance_claim_prediction.git
cd car_insurance_claim_prediction

### 2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
### 3️⃣ Install Dependencies
pip install -r requirements.txt
### 4️⃣ Run the Flask Application
python app.py
The application will be available at http://127.0.0.1:5000/

🛠️ Usage

Launch the web app and enter customer details.
Click "Predict" to get claim probability.
View insights like claim statistics and data visualizations.
📊 Model Performance

Accuracy: 92%
Precision: 89%
Recall: 85%
F1-score: 87%
Algorithm Used: Random Forest / XGBoost
Model evaluation is available in the car_insurance_pred.ipynb Jupyter Notebook.

🤝 Contributing

Contributions are welcome! Follow these steps:

Fork the repo
Create a feature branch:
git checkout -b feature-name
Commit changes:
git commit -m "Added new feature"
Push to GitHub:
git push origin feature-name
Create a Pull Request (PR)

📬 Contact

📧 Email: sruthy-sn91@example.com
🔗 GitHub: @sruthy-sn91
🔗 LinkedIn: Profile

🔥 If you found this project helpful, don't forget to ⭐ the repository! 🚀



