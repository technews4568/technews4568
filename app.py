from flask import Flask, jsonify, request
from flask_cors import CORS
import database

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Sample user data (replace with a real user authentication system)
users = [
    {"id": 1, "username": "user1", "password": "password1"},
    {"id": 2, "username": "user2", "password": "password2"},
]

# Sample bug data (replace with SQLite database queries)
bugs = [
    {"id": 1, "title": "Bug 1", "description": "This is bug 1", "status": "Open", "assignedTo": 1},
    {"id": 2, "title": "Bug 2", "description": "This is bug 2", "status": "In Progress", "assignedTo": 2},
    {"id": 3, "title": "Bug 3", "description": "This is bug 3", "status": "Closed", "assignedTo": 1},
]

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = next((u for u in users if u["username"] == username and u["password"] == password), None)
    if user:
        return jsonify({"success": True, "userId": user["id"]}), 200
    else:
        return jsonify({"success": False, "message": "Invalid credentials"}), 401

@app.route("/api/bugs", methods=["GET"])
def get_bugs():
    # Replace this with actual SQLite database query
    return jsonify(bugs), 200

if __name__ == "__main__":
    app.run(debug=True)
