import requests
import json
import streamlit as st
import pydeck as pdk
import pandas as pd

# load data about people in space from API
space = requests.get('http://api.open-notify.org/astros.json')
space_data = json.loads(space.text)

# load data about location of the ISS
iss = requests.get('http://api.open-notify.org/iss-now.json')
iss_data = json.loads(iss.text)

# assign data about people that should be shown via streamlit app to variables
count = space_data['number']

names = []
for astronaut in space_data['people']:
    names.append(astronaut['name'])

# assign geolocation data to variables
lat = float(iss_data['iss_position']['latitude'])
long = float(iss_data['iss_position']['longitude'])
location = [[lat, long]]

# Title
st.title('Human in space')
#number of human
st.subheader('Number of human in space: ' + str(count))
#name of human
st.subheader('Names of human currently in space:')
st.dataframe(names)

# map location
st.subheader('Current Location of ISS')

df = pd.DataFrame(location,columns =['lat', 'lon'])

st.markdown('These are the current coordinates of the ISS:')
st.dataframe(df)
# st.map(df, zoom=1)

st.subheader('Red dot mark the current coordinates of the ISS:')
st.map(df)

