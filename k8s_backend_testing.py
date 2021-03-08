import requests

try:
    with open("k8s_url.txt", "r") as f:
        url = f.read()
        print(url)
    print(f'{url}/users/4444')
    res = requests.get(f'{url}/users/4444')

    print(res.json())

except Exception as e:
    print(e)



