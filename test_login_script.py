import requests
try:
    resp = requests.post("http://localhost:8000/api/auth/login", json={"email": "admin@healthai.com", "password": "admin123", "role": "ADMIN"})
    print("Response:", resp.status_code, resp.text)
except Exception as e:
    print("Error:", str(e))
