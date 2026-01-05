import joblib

def load_model():
    model = joblib.load(r"disease_model.pkl")
    symptoms = joblib.load(r"symptom_list.pkl")
    return model, symptoms
