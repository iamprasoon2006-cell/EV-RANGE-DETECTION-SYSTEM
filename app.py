import streamlit as st
import pandas as pd
import pickle

# Load dataset (for dropdown values)
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Load encoders
with open("encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

# Title
st.title("🚗 EV Range Prediction System")
st.write("Predict EV range based on vehicle details")

# -------------------------------
# INPUT SECTION
# -------------------------------

make = st.selectbox("Select Manufacturer", sorted(df['Make'].unique()))
year = st.slider("Select Model Year", int(df['Model Year'].min()), int(df['Model Year'].max()))

ev_type = st.selectbox("Select Vehicle Type", sorted(df['Electric Vehicle Type'].unique()))
county = st.selectbox(
    "Select County",
    sorted(df['County'].dropna().astype(str).unique())
)
cafv = st.selectbox("CAFV Eligibility", sorted(df['Clean Alternative Fuel Vehicle (CAFV) Eligibility'].unique()))

# -------------------------------
# ENCODING INPUT (VERY IMPORTANT)
# -------------------------------

def encode_input(value, column):
    le = encoders[column]
    if value in le.classes_:
        return le.transform([value])[0]
    else:
        return 0  # fallback if unseen

input_data = pd.DataFrame({
    'Make': [encode_input(make, 'Make')],
    'Model Year': [year],
    'Electric Vehicle Type': [encode_input(ev_type, 'Electric Vehicle Type')],
    'County': [encode_input(county, 'County')],
    'Clean Alternative Fuel Vehicle (CAFV) Eligibility': [encode_input(cafv, 'Clean Alternative Fuel Vehicle (CAFV) Eligibility')]
})

# -------------------------------
# PREDICTION
# -------------------------------

if st.button("Predict Range"):
    prediction = model.predict(input_data)[0]
    
    st.success(f"🔋 Estimated Electric Range: {round(prediction, 2)} miles")

# -------------------------------
# OPTIONAL: SHOW DATA SAMPLE
# -------------------------------

if st.checkbox("Show Dataset Sample"):
    st.write(df.head())