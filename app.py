import streamlit as st
import pickle

with open('./model/emotion_detection.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_emotion(text):
    predicted_emotion = model.predict([text])
    return predicted_emotion[0]

def main():
    st.title("Emotion Prediction")

    custom_text = st.text_input("Enter your text:")

    if st.button("Predict"):
        if custom_text:
            emotion = predict_emotion(custom_text)
            st.write("Predicted Emotion:", emotion)
        else:
            st.write("Please enter some text to predict the emotion.")

if __name__ == "__main__":
    main()
