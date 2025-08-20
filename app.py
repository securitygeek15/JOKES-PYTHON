from flask import Flask, jsonify
import random

app = Flask(__name__)

import json
with open("jokes.json") as f:
    jokes = json.load(f)

@app.route("/")
def home():
   
    return jsonify(random.choice(jokes))

@app.route("/api/jokes", methods=["GET"])
def get_jokes():
    return jsonify(jokes)

@app.route("/api/jokes/random", methods=["GET"])
def get_random_joke():
    return jsonify(random.choice(jokes))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
