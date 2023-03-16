import streamlit as st
import openai

secrets = st.secrets["openai"]
openai.api_key = secrets["api_key"]

st.title("Itinerary Genie")
st.markdown("Enter the destination, number of days, and your interests, then click 'Generate Itinerary'. Shazam!")

model_engine = "text-davinci-002"
openai.api_key = secrets["api_key"]

def generate_itinerary(destination, days, interests):
    prompt = f"As a specialist in {destination}, devise an all-encompassing and enthralling {days}-day expedition plan that caters to these particular interests: {', '.join(interests)}. The plan should incorporate a wealth of suggestions, including engaging activities, top-rated accommodations, and insider tips that reveal the exceptional charm of the destination. Delve into the destination's rich history, vibrant culture, must-see attractions, and breathtaking natural wonders. For each day of the journey, provide a comprehensive rundown of activities and their significance, ensuring they align with the traveler's interests. Offer practical information such as opening hours, entrance fees, and the best time to visit each attraction, as well as recommendations for nearby dining and shopping options. Paint a vivid and captivating picture of the entire experience, from the morning's first light to the evening's last glimmer. Include anecdotes, lesser-known facts, and insider secrets to truly bring the destination to life."
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
