import streamlit as st
import pandas as pd
import pickle

# Load dataset (for dropdown values)
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Title
st.title("🚗 EV Range Prediction System")

st.write("Predict the electric range of a vehicle based on inputs.")

# Inputs
make = st.selectbox("Select Manufacturer", df['Make'].unique())
year = st.slider("Select Model Year", int(df['Model Year'].min()), int(df['Model Year'].max()))
ev_type = st.selectbox("Select Vehicle Type", df['Electric Vehicle Type'].unique())

# Encoding (same as training)
from sklearn.preprocessing import LabelEncoder

le_make = LabelEncoder()
le_type = LabelEncoder()

df['Make_encoded'] = le_make.fit_transform(df['Make'])
df['Type_encoded'] = le_type.fit_transform(df['Electric Vehicle Type'])

make_encoded = le_make.transform([make])[0]
type_encoded = le_type.transform([ev_type])[0]

# Prediction
if st.button("Predict Range"):
    input_data = pd.DataFrame({
        'Make': [make_encoded],
        'Model Year': [year],
        'Electric Vehicle Type': [type_encoded]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"🔋 Estimated Electric Range: {round(prediction, 2)} miles")