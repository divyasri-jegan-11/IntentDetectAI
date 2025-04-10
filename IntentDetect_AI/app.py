import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

st.title("🧠 IntentDetectAI")
st.write("Multilingual Intent Classifier")

tokenizer = AutoTokenizer.from_pretrained("divyasani11/IntentDetectAI")
model = AutoModelForSequenceClassification.from_pretrained("divyasani11/IntentDetectAI")

text = st.text_input("Enter your query:")
if text:
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
    prediction = torch.argmax(logits, dim=-1).item()
    st.write(f"Predicted intent: {prediction}")
