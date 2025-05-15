import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd

# Load processed data
df = pd.read_csv('../data/processed_data.csv')
X = df.drop('Class', axis=1)
y = df['Class']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42
)

# Train XGBoost
model = xgb.XGBClassifier(
    objective='binary:logistic',
    scale_pos_weight=578,
    max_depth=6,
    learning_rate=0.01,
    tree_method='gpu_hist'  # Remove if no GPU
)

model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))

# Save model
model.save_model('../models/xgb_model.json')