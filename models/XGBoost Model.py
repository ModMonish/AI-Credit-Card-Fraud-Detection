import xgboost as xgb
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib

# Load preprocessed data
df = pd.read_csv('../data/processed_data.csv')
X = df.drop('Class', axis=1)
y = df['Class']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

# Train model
model = xgb.XGBClassifier(
    objective='binary:logistic',
    max_depth=6,
    learning_rate=0.01,
    subsample=0.8,
    colsample_bytree=0.8,
    scale_pos_weight=578,  # 578:1 imbalance ratio
    tree_method='gpu_hist'  # Remove if no GPU
)
model.fit(X_train, y_train)

# Save model
model.save_model('../models/xgb_model.json')

# Evaluation
from sklearn.metrics import classification_report
print(classification_report(y_test, model.predict(X_test)))