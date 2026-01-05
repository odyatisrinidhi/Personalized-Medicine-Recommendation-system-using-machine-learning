import streamlit as st
from model import load_model
from utils import get_description, get_precautions, get_diet, get_medicines

st.set_page_config(page_title="Disease & Medicine Recommendation", layout="centered")
st.title("🩺 personalized Medicine Recommendation System")

# Load model and symptoms
model, symptoms = load_model()

# UI for symptom selection
user_input = st.multiselect("✅ Select your symptoms:", symptoms)

if st.button("🔍 Predict Disease"):
    if not user_input:
        st.warning("Please select at least one symptom.")
    else:
        input_data = [1 if sym in user_input else 0 for sym in symptoms]
        prediction = model.predict([input_data])[0]

        st.success(f"🎯 Predicted Disease: **{prediction}**")
        st.markdown(f"**📖 Description:** {get_description(prediction)}")
        st.markdown(f"**💊 Recommended Medicines:** {', '.join(get_medicines(prediction))}")
        st.markdown(f"**🥗 Diet Plan:** {', '.join(get_diet(prediction))}")
        st.markdown(f"**🛡️ Precautions:** {', '.join(get_precautions(prediction))}")
        st.markdown(f"""
    <div style='
        animation: fadeIn 1s ease-in-out;
        text-align:center;
        font-weight:bold;
        color:red;
    '>
        ⚠️ Warning: Consult a Doctor Before Using Any Medicine ⚠️
    </div>

    <style>
    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}
    </style>
""", unsafe_allow_html=True)



