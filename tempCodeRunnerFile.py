import pyautogui
import time
from datetime import datetime, timedelta
import streamlit as st

# Function to calculate remaining time dynamically
def get_remaining_time():
    current_time = datetime.now()
    target_time = datetime(current_time.year, current_time.month, current_time.day, 12, 0)
    if target_time < current_time:
        target_time += timedelta(days=1)
    remaining_time = target_time - datetime.now()
    return remaining_time

# Function to send countdown messages
def send_countdown_messages():
    while True:
        remaining_time = get_remaining_time()
        if remaining_time.total_seconds() < 5:
            break
        remaining_hours, remainder = divmod(remaining_time.seconds, 3600)
        remaining_minutes, remaining_seconds = divmod(remainder, 60)
        remaining_hours += remaining_time.days * 24
        remaining_time_str = f"{remaining_hours} hours, {remaining_minutes} minutes, and {remaining_seconds} seconds left"
        for char in remaining_time_str:
            pyautogui.typewrite(char)
            time.sleep(0.05)  # Adjust the delay as needed
        pyautogui.press("enter")
        time.sleep(5)


# Streamlit UI
st.set_page_config(page_title="Event Countdown App", page_icon=":alarm_clock:")
st.title("Event Countdown and Message Sender")

event_type = st.text_input("Enter event type (e.g., birthday, anniversary):")

if st.button("Run"):
    st.write(f"Countdown started for {event_type}.")
    send_countdown_messages()
    st.write(f"Message sent for {event_type} at 12:00 AM.")