import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Load dataset (for columns reference)
df = pd.read_csv("flight_prices_clean_data.csv")

st.title(" Flight Price Predictor")

st.write("Enter flight details to predict ticket price")

# Inputs
airline = st.selectbox("Select Airline", df['airline'].unique())
source = st.selectbox("Source City", df['source_city'].unique())
destination = st.selectbox("Destination City", df['destination_city'].unique())
days_left = st.slider("Days Before Departure", 1, 50, 10)
departure_time = st.selectbox("Departure Time", df['departure_time'].unique())
stops = st.selectbox("Number of Stops", df['stops'].unique())
flight_class = st.selectbox("Class", df['class'].unique())

# Create input dataframe
input_df = pd.DataFrame({
    'airline': [airline],
    'source_city': [source],
    'destination_city': [destination],
    'days_left': [days_left],
    'departure_time': [departure_time],
    'stops': [stops],
    'class': [flight_class]
})

# Encode input same as training
input_encoded = pd.get_dummies(input_df)

# Match training columns
model_columns = pickle.load(open("model_columns.pkl", "rb"))
input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

# Prediction
if st.button("Predict Price"):
    prediction = model.predict(input_encoded)
    st.success(f" Estimated Flight Price: ₹{int(prediction[0])}")