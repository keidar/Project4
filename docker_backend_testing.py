import requests

res = requests.get('http://0.0.0.0:5005/users/4444')

print(res.json())

