from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

# Home route → loads your Cat Calculator UI
@app.route("/")
def home():
    return render_template("index.html")

# API route → handle calculation requests
@app.route("/api/calc", methods=["POST"])
def calculate():
    data = request.get_json()
    expression = data.get("expression", "")

    try:
        # Very basic safe evaluation
        # Only allow digits, operators, and decimal point
        allowed = "0123456789+-*/()."
        if not all(char in allowed for char in expression):
            return jsonify({"error": "Invalid input"}), 400

        # Evaluate expression
        result = eval(expression, {"__builtins__": {}}, {})

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": "Calculation error"}), 400


if __name__ == "__main__":
    app.run(debug=True)

