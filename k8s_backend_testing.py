import requests

try:
    f = open("k8s_url.txt", "r")
    url = f.read()
    print(url)
    res = requests.get(f'{url}/users/4444')

    print(res.json())

except Exception as e:
    print(e)



