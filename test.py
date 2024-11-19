import requests

BASE_URL = "http://127.0.0.1:5971"

# Test user credentials
test_users = [
    {"username": "john_doe", "password": "password123"},
    {"username": "invalid_user", "password": "wrong_password"}
]

def test_login():
    print("Testing Login Endpoint:")
    for user in test_users:
        response = requests.post(f"{BASE_URL}/auth/login", json={
            "username": user["username"],
            "password": user["password"]
        })
        if response.status_code == 200:
            data = response.json()
            print(f"  - {user['username']} login successful")
        else:
            print(f"  - {user['username']} login failed. Response: {response.json()}")
    print("Login tests completed.\n")


if __name__ == "__main__":
    print("Starting test...\n")
    test_login()
    print("Test completed successfully.")
