from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np
import pandas as pd
from preprocess import preprocess_input

app = Flask(__name__)

# Load trained model
model = pickle.load(open("models/model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    processed_data = preprocess_input(data)
    prediction = model.predict(processed_data)
    
    result = "Claim will be filed" if prediction[0] == 1 else "No claim"
    return render_template('index.html', prediction_text=result)

@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.get_json()
    processed_data = preprocess_input(data)
    prediction = model.predict(processed_data)
    
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port = 5000, debug=True)
