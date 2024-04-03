from flask import Flask, request
from roberta_base import makePrediction
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def health():
  return "hello there!"

@app.route("/api/todo", methods=['POST'])
def todos():
    query = request.form['query']

    if query :
      res = makePrediction(query)
      return res
    return ""

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
