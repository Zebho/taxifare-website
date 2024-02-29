import streamlit as st

import pandas as pd

import requests
import datetime

import time


# from streamlit_folium import folium_static
# import folium
# import os

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')


st.markdown("""# Calcul ton prix de transport à NYC""")

st.markdown("""# Quelles sont tes informations ? """)

d = st.date_input(
    "When's your pick up date",
    datetime.date(2019, 7, 6))

d = '2012-10-06 2012:10:20'

pickup_longitude = st.number_input('Insert a pickup_longitude')

pickup_latitude = st.number_input('Insert a pickup_latitude')

dropoff_longitude = st.number_input('Insert a dropoff_longitude')

dropoff_latitude = st.number_input('Insert a dropoff_latitude')

passenger_count = st.slider('Select a number of passenger', 1, 8, 1)


dict_request = {
        'pickup_datetime' : d,
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count}

url = 'https://taxifare.lewagon.ai/predict?'

import requests


response = requests.get(
    url,
    params=dict_request,).json()

print(response)
st.write(response)

ShowMap = st.checkbox('Show Map')


if st.button('click me'):
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.005)

    st.write(f"Votre course vous coutera : {round(response['fare_amount'],2)} $ ")

    if ShowMap:

        st.write('Une map iciiiiiiiii')
else:
    pass
