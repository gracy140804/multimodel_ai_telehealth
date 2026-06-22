import requests

url = "https://teleheath-production.up.railway.app/api/auth/register"
payload = {
    "email": "admin@healthai.com",
    "password": "admin123",
    "name": "System Admin",
    "role": "ADMIN"
}

try:
    print(f"Sending registration request to {url}...")
    response = requests.post(url, json=payload)
    print("Status:", response.status_code)
    print("Response:", response.text)
except Exception as e:
    print("Error:", str(e))
