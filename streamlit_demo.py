import streamlit as st

st.title("Chatbot Memory Demo")

st.header("Welcome to the Chatbot Memory Demo")

st.text_input("Enter your message here:")

st.write("Hello, World! ")

st.button("Click me")

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")
    
txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
)

st.write(f"You wrote {len(txt)} characters.")

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)


age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")