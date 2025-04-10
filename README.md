# 🧠 IntentDetectAI

**IntentDetectAI** is a multilingual intent classification system that leverages a fine-tuned BERT model to classify user queries into predefined intents. It supports multiple languages and includes emoji sentiment detection for enhanced conversational AI understanding.

---

## 🔍 Features

- 🌍 **Multilingual intent classification** using a fine-tuned BERT model  
- 😊 **Emoji detection and sentiment visualization**  
- 🧪 Trained on the **MASSIVE** dataset  
- 🎯 **Streamlit app interface** for user-friendly interaction  
- 🚀 **Deployed on Hugging Face Spaces**  

---

## 🧰 Tech Stack

- Python  
- [Transformers (Hugging Face)](https://huggingface.co/docs/transformers)  
- PyTorch  
- Streamlit  
- Hugging Face Datasets  
- Hugging Face Spaces (for deployment)  

---

## 📦 Installation

```bash
git clone https://github.com/your-username/IntentDetectAI.git
cd IntentDetectAI
pip install -r requirements.txt
streamlit run app.py

```
---

📊 Demo

👉 Try the app live on Hugging Face Spaces
[IntentDetectAI](divyasani11/IntentDetect_AI)

---

📁 Project Structure

```bash

IntentDetectAI/
├── app.py                     # Streamlit application
├── model/                     # Fine-tuned model files
├── data/                      # Dataset & preprocessing
├── train_intent_model.ipynb   # Model training notebook
├── requirements.txt           # Required libraries
└── README.md                  # Project description

```

---
💡 How It Works

   - User inputs a query (text with or without emojis).
   - The query is tokenized and passed to a fine-tuned BERT model.
   - The model predicts the most probable intent.
   - The app shows the predicted intent and visualizes any emojis if present.

---

📚 Learnings

 This project demonstrates:

   ✅ Fine-tuning transformer models for intent classification

   ✅ Handling multilingual NLP data and emoji sentiment

   ✅ Streamlit app development

   ✅ Model deployment using Hugging Face Spaces

---

🤝 Contributing


  Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---
📄 License

This project is licensed under the MIT License. See the LICENSE file for details.




