import streamlit as st
import openai

secrets = st.secrets["openai"]
openai.api_key = secrets["api_key"]

st.title("Itinerary Genie")
st.markdown("Enter the destination, number of days, and your interests, then click 'Generate Itinerary'. Shazam!")

model_engine = "text-davinci-002"
openai.api_key = secrets["api_key"]

def generate_itinerary(destination, days, interests):
    prompt = f"As a highly skilled travel expert, your task is to create a unique and unforgettable {days}-day itinerary for travelers seeking an exclusive and off-the-beaten-path experience in {destination}. Focus on the following interests: {', '.join(interests)}. Make sure that there's enough time in each destination as needed. Also, keep in mind the distances between each destination and if it is better to drive or fly. Each day should have a detailed description, including recommendations for meals and accommodations. Use evocative language and sensory-rich details to bring the experience to life. Transport readers to the heart of {destination}, where they can imagine themselves fully immersed in the activities and sights you describe."
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
