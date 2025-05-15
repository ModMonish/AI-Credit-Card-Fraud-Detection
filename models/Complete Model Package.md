# Model Files Description

## xgb_model.json
- Trained XGBoost classifier
- Input shape: (None, 30)
- Output: Fraud probability (0-1)

## scaler.pkl
- RobustScaler for 'Amount' feature
- Usage: transform single value or array

## shap_explainer.pkl
- Pre-fitted SHAP explainer
- Required for real-time explanations

## Retraining Schedule
Nightly cron job:
`0 3 * * * python retrain.py >> logs/retrain.log`