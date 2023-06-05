import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Read data from CSV file in GitHub
url = 'https://raw.githubusercontent.com/Rob-Geurts/Broodstickers/main/StickerLocaties.csv'
df = pd.read_csv(url, sep=';')

# Create map figure
fig = go.Figure(data=go.Scattermapbox(
    lat=df['Latitude'],
    lon=df['Longitude'],
    mode='markers',
    marker=go.scattermapbox.Marker(size=14),
    text=df['Location'],
))

fig.update_layout(
    mapbox_style="open-street-map",
    geo_scope='world',
    autosize=True,
    mapbox=dict(
        center=dict(
            lat=df['Latitude'].mean(),
            lon=df['Longitude'].mean(),
        ),
        zoom=1,
    ),
)

# Create two columns with specified width ratios
col1, col2 = st.columns((3,2))

# Show map in the left column
col1.plotly_chart(fig)

# Select location and show image in the right column
selected_location = col2.selectbox('Select a location', df['Location'])

if col2.button('Show Image'):
    selected_image = df[df['Location'] == selected_location]['ImageURL'].values[0]
    col2.image(selected_image, width=400) # Control the width of the image
