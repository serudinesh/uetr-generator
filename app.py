from flask import Flask, render_template, jsonify
from uetr_generator import generate_uetr

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate")
def generate():
    uetr = generate_uetr()
    return jsonify({"uetr": uetr})

if __name__ == "__main__":
    app.run(debug=True)