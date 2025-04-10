from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from utils import extract_text_from_file

app = Flask(__name__)
CORS(app)  # Frontend ile bağlantı için

# openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/filter", methods=["POST"])
def filter_text():
    data = request.json
    input_text = data.get("text", "")

    prompt = f"Aşağıdaki metindeki ayrımcı, ırkçı, cinsiyetçi, homofobik ifadeleri tespit et ve sansürle:\n\n\"{input_text}\""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # ← burada model adını değiştir
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    result = response.choices[0].message["content"]
    return jsonify({"filtered_text": result})


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    text = extract_text_from_file(file)
    return jsonify({"text": text})


if __name__ == "__main__":
    app.run(debug=True)
