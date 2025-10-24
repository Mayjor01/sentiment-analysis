# Sentiment Analysis Project

## Overview
This project performs **sentiment analysis** on text data using **Python** and **machine learning**.  
The goal is to classify text into **Positive**, **Negative**, or **Neutral** sentiments.  
Data was sourced from **Kaggle**, cleaned, analyzed, modeled, and deployed using **Streamlit**.

![WhatsApp Image 2025-10-24 at 10 24 33_bea7bc6f](https://github.com/user-attachments/assets/62c66a55-ddd8-4a24-bbf7-554c4535f69a)

---

## Process
1. **Data Collection** – Imported dataset from Kaggle.  
2. **Data Cleaning** – Removed duplicates, handled missing data, and cleaned text using **NLTK**.  
3. **EDA** – Visualized sentiment distribution using **Matplotlib** and **Seaborn**.  
4. **Feature Extraction** – Used **TF-IDF Vectorizer** to convert text to numerical features.  
5. **Model Training** – Trained a **Naive Bayes** classifier for sentiment prediction.  
6. **Evaluation** – Measured accuracy, precision, recall, and F1-score.  
7. **Deployment** – Built an interactive **Streamlit app** for live sentiment prediction.

---

## Tools & Libraries
- Python, Pandas, NumPy  
- NLTK, Scikit-learn  
- Matplotlib, Seaborn  
- Streamlit, Pickle  

---

## Run the App
```bash
pip install pandas numpy nltk scikit-learn streamlit
streamlit run app.py
http://localhost:8501/
