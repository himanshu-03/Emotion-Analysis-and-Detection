import streamlit as st
import pickle
import base64

with open('./model/emotion_detection.pkl', 'rb') as f:
    model = pickle.load(f)

with open("assets/gradient.png", "rb") as img_file:
    base64_image = base64.b64encode(img_file.read()).decode('utf-8')

def predict_emotion(text):
    predicted_emotion = model.predict([text])
    return predicted_emotion[0]

def main():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("data:image/png;base64,{base64_image}");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
    with st.container():
        st.markdown(
            """
            <h1 style='text-align: center;'>Emotion Analysis and Detection</h1>
            """,
            unsafe_allow_html=True
        )

        custom_text = st.text_input("Enter your text:")

        if st.button("Predict", key='predict_button'):
            if custom_text:
                emotion = predict_emotion(custom_text)
                st.markdown(f"<p style='font-size: 30px;'>Predicted Emotion: {emotion}</p>", unsafe_allow_html=True)
            else:        
                st.markdown("<p style='font-size: 30px;'>Please enter some text to predict the emotion.</p>", unsafe_allow_html=True)
        st.markdown(
        """
            <style>
            div.stButton > button {
                transition: background-color 0.3s ease;
            }
            div.stButton > button:hover {
                background-color: #090088;
                color: #fff;
                border-color: #fff;
                font-weight: bold;
            }
            </style>
        """,
        unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
