#!/usr/bin/python3
from flask import Flask, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)

# In-memory user data
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password1"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password2"), "role": "admin"}
}

# Basic authentication
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route('/data')
def data():
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return 'OK'

@app.route('/users/<username>')
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    user = users[username]
    user["username"] = username

    return jsonify(user)

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.get_json() is None:
        abort(400, "Not a JSON")

    data = request.get_json()

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    users[data["username"]] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    output = {
        "username": data["username"],
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    return jsonify({"message": "User added", "user": output}), 201

# JWT authentication
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = users.get(username, None)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={"username": username, "role": user["role"]})
        return jsonify(access_token=access_token), 200

    return jsonify({"error": "Bad username or password"}), 401

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# Error handlers for JWT errors
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
