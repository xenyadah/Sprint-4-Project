import streamlit as st
import pandas as pd
import plotly.express as px

vehicles = pd.read_csv('vehicles_us.csv')
vehicles['manufacturer'] = vehicles['model'].apply(lambda x:x.split()[0])

# create a text header above the dataframe
st.header('Data viewer') 
# display the dataframe with streamlit
st.dataframe(vehicles)

st.header('Vehicle types by manufacturer')
# create a plotly histogram figure
fig = px.histogram(vehicles, x='manufacturer', color='type')
# display the figure with streamlit
st.write(fig)

st.header('Histogram of `condition` vs `price`')
fig = px.histogram(vehicles, x='price', color='condition')
st.write(fig)

st.header('Compare price distribution between manufacturers')
# get a list of car manufacturers
manufac_list = sorted(vehicles['manufacturer'].unique())
# get user's inputs from a dropdown menu
manufacturer_1 = st.selectbox(
                              label='Select manufacturer 1', # title of the select box
                              options=manufac_list, # options listed in the select box
                              index=manufac_list.index('ford') # default pre-selected option
                              )
# repeat for the second dropdown menu
manufacturer_2 = st.selectbox(
                              label='Select manufacturer 2',
                              options=manufac_list, 
                              index=manufac_list.index('nissan')
                              )
# filter the dataframe 
mask_filter = (vehicles['manufacturer'] == manufacturer_1) | (vehicles['manufacturer'] == manufacturer_2)
vehicles_filtered = vehicles[mask_filter]

# add a checkbox if a user wants to normalize the histogram
normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None

# create a plotly histogram figure
fig = px.histogram(vehicles_filtered,
                      x='price',
                      nbins=30,
                      color='manufacturer',
                      histnorm=histnorm,
                      barmode='overlay')
# display the figure with streamlit
st.write(fig)