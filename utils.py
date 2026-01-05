import pandas as pd

def get_description(disease):
    df = pd.read_csv(r"data/description.csv")
    df.columns = df.columns.str.strip()
    result = df[df['Disease'].str.lower() == disease.lower()]
    return result['Description'].values[0] if not result.empty else "No description found."

def get_precautions(disease):
    df = pd.read_csv(r"data\precautions_df.csv")
    df.columns = df.columns.str.strip()
    row = df[df['Disease'].str.lower() == disease.lower()]
    return row.values[0][1:] if not row.empty else ["No data"]

def get_diet(disease):
    df = pd.read_csv(r"data/diets.csv")
    df.columns = df.columns.str.strip()
    row = df[df['Disease'].str.lower() == disease.lower()]
    return row.values[0][1:] if not row.empty else ["No data"]

def get_medicines(disease):
    df = pd.read_csv(r"data/medications.csv")
    df.columns = df.columns.str.strip()
    row = df[df['Disease'].str.lower() == disease.lower()]
    return row.values[0][1:] if not row.empty else ["No data"]
