import pandas as pd
import streamlit as st
import pickle
import bz2
import numpy as np
st.set_page_config(page_title="Predictive Price App", layout="wide")

with open('model.pkl', 'rb') as file:
    df = pickle.load(file)


import bz2
import pickle
import sys

file_path = 'pipeline.pkl.bz2'

try:
    with bz2.BZ2File(file_path, 'rb') as file:
        pipeline = pickle.load(file)
except ModuleNotFoundError as e:
    print(f"ModuleNotFoundError: {e}", file=sys.stderr)
    raise






st.header('Enter your inputs ')

property_type = st.selectbox('Property Type', ['flat', 'house'])

sector = st.selectbox('sector' , sorted(df ['sector'].unique().tolist()) )

bedroom  = float(st.selectbox('bedRoom', sorted(df['bedRoom'].unique().tolist()) ))

bathroom  = float(st.selectbox('bathroom', sorted(df['bathroom'].unique().tolist()) ))

balcony  = st.selectbox('balcony', sorted(df['balcony'].unique().tolist()) )

property_age = st.selectbox('property_age', sorted(df['agePossession'].unique().tolist()))

built_up_area = float(st.number_input('Built_up_area'))

servent_room = float(st.selectbox('servent_room', ['0.0', '1.0']))

store_room = float(st.selectbox('store_room', ['0.0', '1.0']))

furnishing = st.selectbox('furnishing', sorted(df['furnishing_type'].unique().tolist()))

luxury_category = st.selectbox('luxury_category', sorted(df['luxury_category'].unique().tolist()))

floor_category = st.selectbox('floor_category', sorted(df['floor_category'].unique().tolist()))


if st.button('Predict'):

    data = [[property_type, sector, bedroom, bathroom, balcony,property_age, built_up_area, servent_room , store_room , furnishing , luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    one_df = pd.DataFrame(data , columns=columns)
    st.dataframe(one_df)

    base_price =  np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.21
    high = base_price + 0.21
    st.text("The Price of the {} is between {} CR and {} CR".format(property_type, round(low,2), round(high,2)))
