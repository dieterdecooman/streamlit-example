import streamlit as st
import pandas as pd

# Create a DataFrame to store registered participants
participants_df = pd.DataFrame(columns=['Name', 'Date'])

# Sample data for rides
rides_data = [
    {'Date': '2023-07-01', 'Location': 'Park A'},
    {'Date': '2023-07-05', 'Location': 'Park B'},
    {'Date': '2023-07-10', 'Location': 'Park C'}
]
rides_df = pd.DataFrame(rides_data)

# Streamlit application header
st.title("Cycling Calendar and Registration")

# Display the table of rides with registration button
st.subheader("Upcoming Rides")
for index, row in rides_df.iterrows():
    ride_date = row['Date']
    ride_location = row['Location']
    register_button = st.button(f"Register for {ride_date} - {ride_location}")
    
    if register_button:
        participant_name = st.text_input("Enter your name")
        if participant_name:
            participants_df = participants_df.append({'Name': participant_name, 'Date': ride_date}, ignore_index=True)
            st.success(f"{participant_name} successfully registered for {ride_date} - {ride_location}")

# Display registered participants
st.subheader("Registered Participants")
st.dataframe(participants_df)