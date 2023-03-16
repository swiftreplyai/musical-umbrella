import streamlit as st
import openai

secrets = st.secrets["openai"]
openai.api_key = secrets["api_key"]

st.title("Itinerary Generator with ChatGPT")
st.markdown("Enter the destination, number of days, and your interests, then click 'Generate Itinerary'.")

model_engine = "text-davinci-002"
openai.api_key = secrets["api_key"]

def generate_itinerary(destination, days, interests):
    prompt = f"Create a detailed itinerary for a {days}-day trip to {destination} with a focus on the following interests: {', '.join(interests)}. Include recommended activities, accommodations, and other suggestions."

    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

def main():
    destination = st.text_input("Enter the destination:")
    days = st.number_input("Enter the number of days:", min_value=1, value=1)
    interests = st.multiselect("Select your interests:", options=['Culture', 'Adventure', 'Food', 'Nature', 'Shopping', 'Nightlife', 'Relaxation'])

    if st.button("Generate Itinerary"):
        if destination and days and interests:
            generated_itinerary = generate_itinerary(destination, days, interests)
            st.write(generated_itinerary)
        else:
            st.write("Please provide all the required information.")

if __name__ == '__main__':
    main()
