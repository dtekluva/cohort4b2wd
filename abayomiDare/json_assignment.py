import requests

response = requests.get("http://datanigeria.pythonanywhere.com/play/dare/106799")
data = response.json()
print(data)
