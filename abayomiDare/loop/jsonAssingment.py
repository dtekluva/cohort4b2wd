import requests

user_name = 'Dare'

for number in range(100000, 999999):
    

    response = requests.get(f'http://datanigeria.pythonanywhere.com/play/{user_name}/{number}')

    data = response.json()
    print(data)

    if data["status"] == True:
        break