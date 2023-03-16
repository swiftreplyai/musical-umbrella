# Step 1: Install necessary libraries
# !pip install streamlit
# !pip install openai

# Step 2: Import required modules
import streamlit as st
import openai

secrets = st.secrets["openai"]
openai.api_key = secrets["api_key"]

# Step 3: Initialize Streamlit app
st.title("Itinerary Generator with ChatGPT")

# Step 4: Set up app layout and widgets
destination = st.text_input("Enter the destination:")
days = st.number_input("Enter the number of days:", min_value=1, value=1)
interests = st.multiselect("Select your interests:", options=['Culture', 'Adventure', 'Food', 'Nature', 'Shopping', 'Nightlife', 'Relaxation'])

generate_button = st.button("Generate Itinerary")

# Step 5: Create a function to generate itinerary using ChatGPT
def generate_itinerary(destination, days, interests):
    openai.api_key = secrets["api_key"]
    prompt = f"Create a detailed itinerary for a {days}-day trip to {destination} with a focus on the following interests: {', '.join(interests)}. Include recommended activities, accommodations, and other suggestions."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Step 6: Call the function with the user's input destination, days, and interests
if generate_button:
    if destination and days and interests:
        generated_itinerary = generate_itinerary(destination, days, interests)

        # Step 7: Display the generated itinerary in the Streamlit app
        st.write(generated_itinerary)
    else:
        st.write("Please provide all the required information.")
