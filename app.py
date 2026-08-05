from flask import Flask, jsonify
from calculator import add

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Calculator API Running"
    })

@app.route("/add/<int:a>/<int:b>")
def add_numbers(a, b):
    return jsonify({
        "result": add(a, b)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)