import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from PIL import Image

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Prediction", "Analysis"])


with open('sentiment.pkl', 'rb') as file:
    model = pickle.load(file)

with open('vectorizer.pkl', 'rb') as file:
    vect = pickle.load(file)

# if page == "Homepage":
#     st.title('Sentiment analysis app')
#     st.toast('welcome to the sentiment analysis app')
#     st.balloons()
#     # homepage()

if page == "Prediction":
    text = st.text_area('Enter your text :')
    st.toast('Welcome to the prediction page')
    
    if st.button("Predict"):
        if text.strip():
            vecto = vect.transform([text])  
            prediction = model.predict(vecto)
            # st.successs(f"Predicted sentiment: {prediction[0]}")
            if prediction[0] == "Positive":
                st.success(f"Predicted sentiment: {prediction[0]}")
            
            if prediction[0] == "Negative":
                st.error(f"Predicted sentiment: {prediction[0]}")
            
            if prediction[0] == "Neutral":
                st.info(f"Predicted sentiment: {prediction[0]}")


            # st.balloons()
        else:
            st.error("Please enter some text first!")

        st.feedback()

    
    image = Image.open(r"C:\Users\USER\Pictures\Saved Pictures\collage-customer-experience-concept.jpg")
    st.image(image, caption="Sentiment Visualization", use_container_width=True)


    # prediction_page()
    # st.toggle('jkkjk')

elif page == "Analysis":
    if st.toggle('Turn on to see the analysis associated with the data used for modeling.'):


        senti_df = pd.read_csv('sen_df.csv')
        st.toast('Welcome to the analysis page')
        if 'sentiment' in senti_df.columns:
            st.subheader("📊 Sentiment distribution in the dataset")
            fig, ax = plt.subplots()
            senti_df['sentiment'].value_counts().plot(kind='bar', ax=ax , color=['gray', 'g', 'r'])
            ax.set_title("Sentiment distribution")
            st.pyplot(fig)