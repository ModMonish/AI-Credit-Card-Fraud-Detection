import streamlit as st
import xgboost as xgb
import pandas as pd

# Load model
model = xgb.XGBClassifier()
model.load_model('../models/xgb_model.json')

st.title('🔍 Real-Time Fraud Detection')

# Input form
col1, col2 = st.columns(2)
with col1:
    amount = st.number_input('Transaction Amount ($)')
with col2:
    hour = st.slider('Hour of Day', 0, 23)

# Prediction
if st.button('Check Fraud Risk'):
    features = [hour, amount] + [0]*28  # Placeholder for PCA features
    proba = model.predict_proba([features])[0][1]
    
    st.metric("Fraud Probability", f"{proba*100:.2f}%")
    if proba > 0.7:
        st.error('🚨 High fraud risk!')
    elif proba > 0.3:
        st.warning('⚠️ Moderate risk')
    else:
        st.success('✅ Low risk')