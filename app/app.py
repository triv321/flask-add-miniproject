from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "I LOVE MY CUTU 😘"

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")

    if num1 is None or num2 is None:
        return jsonify({"error": "Missing input"}), 400

    try:
        result = float(num1) + float(num2)
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Invalid Input"}), 400

    return jsonify({"result": result}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)