import os
import pymysql
import json
from dotenv import load_dotenv
from pathlib import Path

# Creds
env_path = Path('') / '.environ'
load_dotenv(dotenv_path=env_path)
db_table = os.environ['DB_TABLE']


# Establish connection to DB
def get_con():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user=os.environ['USER_NAME'], passwd=os.environ['PASSWD'],
                           db=db_table, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    conn.autocommit(True)
    cursor = conn.cursor()

    return conn , cursor

#Close connection to DB
def close_conn():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user=os.environ['USER_NAME'], passwd=os.environ['PASSWD'],
                           db=db_table, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.close()
    conn.close()


# Insert data into table
def insert_user(user_id, user_name, creation_date):
    conn, cursor = get_con()
    cursor.execute(f"INSERT into {db_table}.users VALUES (%s , %s , %s )",
                   (user_id, user_name, creation_date))
    # Insert to table with datetime variable
    cursor.execute(f"INSERT into {db_table}.usersExtra VALUES (%s , %s , now())",
                   (user_id, user_name))
    close_conn()

# Updating data inside the table
def update_user(name ,user_id ):
    conn, cursor = get_con()
    cursor.execute(f"UPDATE {db_table}.users SET user_name = %s WHERE user_id =  %s", (name, user_id))
    close_conn()

#Delete user from table
def delete_user(user_id):
    conn, cursor = get_con()
    cursor.execute(f"DELETE FROM {db_table}.users WHERE user_id = %s", (user_id))
    close_conn()

#get user by user id
def get_user_id(user_id):
    conn, cursor = get_con()
    cursor.execute(f"SELECT * FROM {db_table}.users WHERE user_id = %s", (user_id))
    for row in cursor:
        name = row['user_name']
    close_conn()
    return name

#get users table
def get_table():
    conn, cursor = get_con()
    cursor.execute(f"SELECT * FROM {db_table}.users;")
    result = cursor.fetchall()
    close_conn()

    return json.dumps(result)

#return users_id column
def get_all_users_ids():
    conn, cursor = get_con()
    cursor.execute(f"SELECT user_id FROM {db_table}.users ")
    result = cursor.fetchall()
    close_conn()
    return result









