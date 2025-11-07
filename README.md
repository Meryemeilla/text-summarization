# 🧠 Text Summarization Project using BART, T5 and Flask

## 📘 Overview

This project focuses on **automatic text summarization** using **Transformer-based models** such as **BART**, **T5-small**, and **PEGASUS** from Hugging Face.  
It aims to condense long English texts into concise summaries while preserving the main ideas.

The final solution includes a **Flask web application** that allows users to input text and instantly receive a generated summary.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Meryemeilla/text-summarization.git
cd text-summarization
```
### 2️⃣ Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate   # On Linux/Mac
```
### 🚀 Run the Flask Application
```bash
python app.py
```
Then open your browser at:
👉 http://127.0.0.1:5000

You can enter any paragraph in English and get an instant summary.

---
## 🧠 Models Used
| Model | Description | Library |
|-------|-------------|---------|
| BART-base | Abstractive summarization model fine-tuned on CNN/DailyMail | 🤗 Transformers |
| T5-small | Lightweight text-to-text model for summarization | 🤗 Transformers |


---

## 📊 Evaluation Metrics
To evaluate the models, the following metrics were used:

|Metric |	Description|
|-------|-------------|
|ROUGE-1 |	Word-level overlap between reference and prediction|
|ROUGE-2 |	Bigram overlap|
|ROUGE-L |	Longest common subsequence between texts|
|BLEU |	N-gram precision metric for text generation|

---

## 🧮 Example
Input Text:

"New study shows a 30% lower risk of cardiovascular issues among Mediterranean diet followers. Researchers followed more than 25,000 participants over a decade, comparing those who followed the diet with those who consumed more processed foods."

Generated Summary:

"People following a Mediterranean diet have a 30% lower risk of heart problems."

---

## 🌐 Technologies Used
🐍 Python 3.11

🤗 Transformers (Hugging Face)

🔥 PyTorch

🌸 Flask

📊 CNN/DailyMail Dataset

---

## 💡 Future Improvements
Deploy the Flask app using Render, Streamlit, or Hugging Face Spaces

Add multilingual summarization support

Integrate a user interface with Bootstrap or Tailwind

Fine-tune models on custom datasets for specific domains (e.g., medical, legal, news)




