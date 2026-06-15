#!/usr/bin/python3
"""
A lightweight RESTful API development using Flask.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to hold user data in memory (empty by default for checker)
users = {}


@app.route("/")
def home():
    """Root endpoint welcoming users."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all stored usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """Returns the operational status of the API."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns full details of a specific user."""
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Parses and adds a new user into the memory dictionary."""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
