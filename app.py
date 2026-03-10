from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")

# Function to get response
def my_output(query):
    response = model.generate_content(query)
    return response.text

# Streamlit UI
st.set_page_config(page_title="SWAT Chatbot")
st.header("SWAT Chatbot")

user_input = st.text_input("Input", key="input")

submit = st.button("Ask Your Query")

if submit:
    response = my_output(user_input)
    st.subheader("The Response is:")
    st.write(response)