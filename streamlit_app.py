import streamlit as st
import requests

# Set up the Streamlit app
st.title("Student Grades Analysis")
st.write("This app interacts with a FastAPI backend to analyze student grades.")

# Define the FastAPI endpoint
api_url = "https://fastapi-backend-9n3a.onrender.com/query"
#api_url = "https://9103-71-81-132-14.ngrok-free.app/query"

# Create a form for user input
query = st.text_input("Enter your query", "")

if st.button("Submit"):
    if query:
        # Make a POST request to the FastAPI backend
        response = requests.post(api_url, json={"text": query})
        
        if response.status_code == 200:
            result = response.json().get("result", "No result found")
            st.write("Response from the API:")
            st.write(result)
        else:
            st.write("Error:", response.status_code)
    else:
        st.write("Please enter a query.")
