from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user data (for example purposes)
USERS = {
    "john_doe": {"password": "password123"},
}


# Route: Authenticate user
@app.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    # Check if the username exists and password matches
    if username not in USERS or USERS[username]["password"] != password:
        return jsonify({"message": "Invalid username or password"}), 401

    # Successful login
    return jsonify({
        "message": "Login successful",
        "username": username,
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5971)
