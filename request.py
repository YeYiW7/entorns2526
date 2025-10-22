import requests

url = "https://api.chucknorris.io/jokes/categories"
response = requests.get(url)

if response.status_code == 200:
    print("✅ Èxit!")
    print(response.text)
else:
    print(f"❌ Error {response.status_code}")
