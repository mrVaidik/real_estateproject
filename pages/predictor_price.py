import streamlit as st
import pandas as pd
import pickle
import bz2
import numpy as np

st.set_page_config(page_title="Predictive Price App", layout="wide")

@st.cache_data
def load_data():
    with open('model.pkl', 'rb') as file:
        df = pickle.load(file)
    return df

@st.cache_resource
def load_pipeline():
    with bz2.BZ2File('pipeline.pkl.bz2', 'rb') as file:
        pipeline = pickle.load(file)
    return pipeline

df = load_data()
pipeline = load_pipeline()

st.header('Enter your inputs')

property_type = st.selectbox('Property Type', ['flat', 'house'])
sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))
bedroom = float(st.selectbox('Bedroom', sorted(df['bedRoom'].unique().tolist())))
bathroom = float(st.selectbox('Bathroom', sorted(df['bathroom'].unique().tolist())))
balcony = st.selectbox('Balcony', sorted(df['balcony'].unique().tolist()))
property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))
built_up_area = float(st.number_input('Built-up Area'))
servent_room = st.selectbox('Servant Room', ['no', 'yes'])
store_room = st.selectbox('Store Room', ['no', 'yes'])
furnishing = st.selectbox('Furnishing', sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):
    # Convert 'yes'/'no' to 1.0/0.0 for the model
    servent_room_value = 1.0 if servent_room == 'yes' else 0.0
    store_room_value = 1.0 if store_room == 'yes' else 0.0

    data = [[property_type, sector, bedroom, bathroom, balcony, property_age, built_up_area, servent_room_value, store_room_value, furnishing, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony', 'agePossession', 'built_up_area', 'servant room', 'store room', 'furnishing_type', 'luxury_category', 'floor_category']
    one_df = pd.DataFrame(data, columns=columns)
    st.dataframe(one_df)

    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.21
    high = base_price + 0.21
    st.header(f"The Price of the {property_type} is between {round(low, 2)} CR and {round(high, 2)} CR")

