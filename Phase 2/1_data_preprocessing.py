import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import RobustScaler
import warnings
warnings.filterwarnings('ignore')

def preprocess_data():
    # Load data
    df = pd.read_csv('../data/creditcard.csv')
    
    # Handle class imbalance
    smote = SMOTE(sampling_strategy=0.2, random_state=42)
    X_res, y_res = smote.fit_resample(df.drop('Class', axis=1), df['Class']
    
    # Scale numerical features
    scaler = RobustScaler()
    X_res['Amount'] = scaler.fit_transform(X_res[['Amount']])
    
    # Save processed data
    X_res['Class'] = y_res
    X_res.to_csv('../data/processed_data.csv', index=False)
    return X_res, y_res

if __name__ == "__main__":
    preprocess_data()