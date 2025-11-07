import datetime
from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

app = Flask(__name__)

# -----------------------------------------------------
#  Charger ton modèle préféré (ici T5-small par défaut)
# -----------------------------------------------------
MODEL_PATH = r"C:\Users\lenovo\final_model"  # change si tu veux BART ou PEGASUS
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)

# -----------------------------------------------------
#  Fonction de génération de résumé
# -----------------------------------------------------
def generate_summary(text, max_length=150):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    summary_ids = model.generate(
        **inputs,
        max_length=max_length,
        num_beams=4,
        early_stopping=True
    )
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# -----------------------------------------------------
#  Routes Flask
# -----------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    summary = None
    text_input = ""
    if request.method == "POST":
        text_input = request.form["text"]
        max_len = int(request.form.get("max_len", 150))
        if text_input.strip():
            summary = generate_summary(text_input, max_length=max_len)
    return render_template("index.html", summary=summary, text_input=text_input, now=datetime.datetime.now())

# -----------------------------------------------------
#  Lancer le serveur
# -----------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
