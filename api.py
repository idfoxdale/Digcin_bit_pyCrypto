# api.py
from flask import Flask, jsonify
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

# Define route for /
@app.route("/", methods=["GET"])
def index():
    return "Welcome to the Blockchain API!"

# Define route for /api/transactions
@app.route("/api/transactions", methods=["GET"])
def get_transactions():
    transactions = []
    for block in blockchain.chain:
        transactions.extend(block.transactions)
    return jsonify(transactions)

# Define route for /favicon.ico
@app.route("/favicon.ico")
def favicon():
    # Return an empty response with 204 No Content status code
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
