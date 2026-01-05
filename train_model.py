import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load and clean data
df = pd.read_csv(r"data/Training.csv")
df.columns = df.columns.str.strip()
X = df.drop('prognosis', axis=1)
y = df['prognosis']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and symptom list
joblib.dump(model, "disease_model.pkl")
joblib.dump(X.columns.tolist(), "symptom_list.pkl")

print("✅ Model and symptom list saved.")
