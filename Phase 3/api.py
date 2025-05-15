from flask import Flask, request, jsonify
import xgboost as xgb
import numpy as np

app = Flask(__name__)
model = xgb.XGBClassifier()
model.load_model('../models/xgb_model.json')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [
        data['hour'],
        data['amount'],
        *data.get('pca_features', [0]*28)
    ]
    proba = model.predict_proba([features])[0][1]
    return jsonify({
        'fraud_probability': float(proba),
        'risk_level': 'high' if proba > 0.7 else 'moderate' if proba > 0.3 else 'low'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)