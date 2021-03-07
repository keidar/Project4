import requests
from db_connector import *

try:
    #Post new user data to DB
    res = requests.post('http://127.0.0.1:5000/users/6666', json={"user_name": "Dvir"})

    #submit that new user inserted to DB
    check_insert = requests.get('http://127.0.0.1:5000/users/6666')
    

    #show all stored data on DB table
    table = get_table()
    table=json.loads(table)


    #print results
    print(res.json())
    print(check_insert.json())
    for i in table:
        print(i)
except:
    print("test failed")
