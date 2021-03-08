import requests

try:
    f = open("k8s_url.txt", "r")
    url = f.read()
    print(url)
    print(f'http://{url}/users/4444')
    res = requests.get(f'http://{url}/users/4444')

    print(res.json())

except Exception as e:
    print(e)



