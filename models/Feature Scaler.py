from sklearn.preprocessing import RobustScaler
import joblib

scaler = RobustScaler()
scaler.fit(X_train[['Amount']])  # Only scale Amount feature

joblib.dump(scaler, '../models/scaler.pkl')