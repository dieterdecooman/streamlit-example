import streamlit as st
from stravalib import Client

def get_strava_activities(access_token):
    client = Client(access_token=access_token)
    activities = client.get_activities(limit=10)
    distances = []
    speeds = []
    for activity in activities:
        distances.append(activity.distance.num / 1000)  # Convert to kilometers
        speeds.append(activity.average_speed.num * 3.6)  # Convert to km/h
    return distances, speeds

def calculate_statistics(distances, speeds):
    total_distance = sum(distances)
    average_speed = sum(speeds) / len(speeds)
    return total_distance, average_speed

def main():
    st.title("Strava Ride Statistics")
    access_token = st.text_input("Enter your Strava access token:")
    if access_token:
        try:
            distances, speeds = get_strava_activities(access_token)
            total_distance, average_speed = calculate_statistics(distances, speeds)
            st.write("Total Distance:", total_distance, "km")
            st.write("Average Speed:", average_speed, "km/h")
        except:
            st.write("Error: Unable to fetch Strava activities. Please check your access token.")

if __name__ == "__main__":
    main()
