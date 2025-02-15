import streamlit as st

# Page Title
st.title("Username Collector App")

# Initialize session state for storing usernames
if 'usernames' not in st.session_state:
    st.session_state.usernames = []

# Input field for username
username = st.text_input("Enter a username:")

# Button to add username
if st.button("Add Username"):
    if username:
        st.session_state.usernames.append(username)
        st.success(f"Username '{username}' added successfully!")
    else:
        st.warning("Please enter a username.")

# Display the list of usernames
st.subheader("List of Usernames:")
if st.session_state.usernames:
    for i, user in enumerate(st.session_state.usernames, 1):
        st.write(f"{i}. {user}")
else:
    st.write("No usernames added yet.")
