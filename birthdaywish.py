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
        remaining_time_str = f"{remaining_hours} hours, {remaining_minutes} minutes, and {remaining_seconds} seconds left "
        for char in remaining_time_str:
            pyautogui.typewrite(char)
            time.sleep(0.05)  # Adjust the delay as needed
        pyautogui.press("enter")
        time.sleep(4)

# Streamlit UI
st.set_page_config(page_title="Event Countdown App", page_icon=":alarm_clock:")
st.title("Event Countdown and Message Sender")

event_type = st.text_input("Enter event type (e.g., birthday, anniversary):")

if st.button("Run"):
    st.write(f"Countdown started for {event_type}.")
    send_countdown_messages()
    st.write(f"Message sent for {event_type} at 12:00 PM.")




















# import pyautogui
# import time
# from datetime import datetime, timedelta


# # List of unique friendship quotes
# friendship_quotes = [
#     "True friends are those who laugh, cry, and walk with you.5 hours and 25 minutes left to your birghtday left",
#     "Friendship is not about how many times we talk, but how genuine the connection is.",
#     "Friendship is the bond where people say, 'Wherever you go, I'm with you.",
#     # Add more quotes here
# ]

# # Function to send countdown messages
# def send_countdown_messages():
#     # Get the current time
#     current_time = datetime.now()
#     # Adjust the current time to be 10 minutes earlier
#     current_time -= timedelta(minutes=10)
#     # Calculate the remaining time until midnight
#     remaining_time = datetime(current_time.year, current_time.month, current_time.day, 23, 50) - current_time
    
#     # Get the remaining hours and minutes
#     remaining_hours, remaining_minutes = divmod(remaining_time.seconds // 60, 60)
    
#     # If less than 1 hour left, only show minutes
#     if remaining_hours < 1:
#         remaining_time_str = f"{remaining_minutes} minutes"
#     else:
#         remaining_time_str = f"{remaining_hours} hours and {remaining_minutes} minutes left to your birghtday"
    
#     # Initialize index of last sent quote
#     last_sent_index = -1
    
#     # Loop until midnight
#     while True:
#         # Get the next friendship quote
#         last_sent_index = (last_sent_index + 1) % len(friendship_quotes)
#         quote = friendship_quotes[last_sent_index]
        
#         # Construct the message with the remaining time and the next friendship quote
#         message = f"{remaining_time_str} left\n{quote}"
        
#         # Typing the message
#         pyautogui.typewrite(message)
#         # Sending the message by pressing 'Enter'
#         pyautogui.press("enter")
        
#         # Wait for 1 minute before sending the next message
#         time.sleep(60)
        
#         # Decrement the remaining time by 1 minute
#         remaining_minutes -= 1
        
#         # Check if countdown time reached 0
#         if remaining_hours == 0 and remaining_minutes == 0:
#             break
        
#         # Update remaining time hours and minutes
#         if remaining_minutes == 0:
#             remaining_hours -= 1
#             remaining_minutes = 59

# # Function to send birthday wishes with friendship quotes
# def send_birthday_wishes():
#     # Birthday message with friendship quotes
#     birthday_message = "🎉🎂 Happy Birthday! 🎂🎉\n1. \"A true friend is one who overlooks your failures and tolerates your success!\" - Doug Larson\n2. \"Friendship is born at that moment when one person says to another: 'What! You too? I thought I was the only one.'\" - C.S. Lewis\n3. \"Friendship is the only cement that will ever hold the world together.\" - Woodrow Wilson"
    
#     # Typing the birthday message
#     pyautogui.typewrite(birthday_message)
    
#     # Sending the message by pressing 'Enter'
#     pyautogui.press("enter")

# # Start sending messages
# send_countdown_messages()
# # Send birthday wishes at midnight
# send_birthday_wishes()
# """
# Sends countdown messages with friendship quotes until midnight, when it sends a birthday message.

# The `send_countdown_messages()` function is responsible for the following:
# - Calculates the remaining time until midnight in hours and minutes.
# - Loops until midnight, sending a message every minute that includes the remaining time and a friendship quote.
# - Updates the remaining time by decrementing the minutes, and adjusting the hours if the minutes reach 0.
# """
