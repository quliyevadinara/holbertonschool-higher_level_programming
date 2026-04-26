#!/usr/bin/python3
"""
Task 04 - Simple API using Flask
Python 3.9
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# IMPORTANT: Do not include testing data when pushing code
users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/data", methods=["GET"])
def data():
    """Return list of usernames"""
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    # Ensure JSON body
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Store full object; ensure it contains username
    user_obj = dict(payload)
    user_obj["username"] = username
    users[username] = user_obj

    return jsonify({"message": "User added", "user": user_obj}), 201


if __name__ == "__main__":
    app.run()
