import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load dataset (Representing your Google Cloud training data)
def train_fraud_model(data_path):
    df = pd.read_csv(data_path)

    # Features: amount, time, location_score, device_id_numeric
    # Target: is_fraud (0 or 1)
    X = df[['amount', 'hour_of_day', 'location_risk_score', 'velocity_score']]
    y = df['is_fraud']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and Train Random Forest
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    print("--- Fraud Detection Report ---")
    print(classification_report(y_test, y_pred))
    return model

if __name__ == "__main__":
    print("Initializing Fraud Detection Training...")
