import streamlit as st
import google.generativeai as genai

# Configure the API key for the Generative AI
genai.configure(api_key="AIzaSyB4tk6azgrb__-VQSgsNT2BW49ABjwaxJiI")

# Define the system prompt
sys_prompt = """You are a helpful AI Tutor for Data Science. 
Students will ask you doubts related to various topics in data science.
You are expected to reply in as much detail as possible. 
Make sure to take examples while explaining a concept.
If a student asks any question outside the data science scope, 
politely decline and tell them to ask a question from the data science domain only."""

# Initialize the generative model
model_name = "models/gemini-1.5-flash"

st.title("Data Science Tutor Application")

# Create input fields and button
user_prompt = st.text_input("Enter your query:", placeholder="Type your query here...")
btn_click = st.button("Generate Answer")

# Handle button click
if btn_click:
    if user_prompt.strip():  # Ensure the user entered a prompt
        try:
            # Generate a response using the model
            response = genai.generate_text(
                model=model_name,
                prompt=user_prompt,
                system_prompt=sys_prompt
            )
            # Display the response
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query before clicking the button.")