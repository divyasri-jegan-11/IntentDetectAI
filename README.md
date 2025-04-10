🧠 IntentDetectAI
<br>
IntentDetectAI is a multilingual intent classification system that leverages a fine-tuned BERT model to classify user queries into predefined intents. It supports multiple languages and includes emoji sentiment detection for enhanced conversational AI understanding.

🔍 Features
🌍 Multilingual intent classification using a fine-tuned BERT model

😊 Emoji detection and sentiment visualization

🧪 Trained on the MASSIVE dataset

🎯 Streamlit app interface for user-friendly interaction

🚀 Deployed on Hugging Face Spaces

🧰 Tech Stack
Python

Transformers (Hugging Face)

PyTorch

Streamlit

Hugging Face Datasets

Hugging Face Spaces (for deployment)

📦 Installation
bash
Copy code
git clone https://github.com/your-username/IntentDetectAI.git
cd IntentDetectAI
pip install -r requirements.txt
streamlit run app.py
📊 Demo
👉 Try the app live on Hugging Face Spaces

📁 Project Structure
bash
Copy code
IntentDetectAI/
├── app.py                 # Streamlit application
├── model/                 # Fine-tuned model files
├── data/                  # Dataset & preprocessing
├── train_intent_model.ipynb # Model training notebook
├── requirements.txt       # Required libraries
└── README.md              # Project description
💡 How It Works
User inputs a query (text with or without emojis).

The query is tokenized and passed to a BERT-based model.

The model predicts the most probable intent.

The app shows the intent and visualizes emojis if present.

📚 Learnings
This project demonstrates:

Fine-tuning transformer models for classification

Handling multilingual NLP data

Streamlit app development and deployment

Model deployment using Hugging Face Spaces

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first.

📄 License
MIT

