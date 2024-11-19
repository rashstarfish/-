import json
import requests
import phoenixdb
import phoenixdb.cursor


def get_testab():
    testab = requests.get('http://localhost:3000/').text
    return testab

def get_hotelUuidKey():
    hotelUuidKey = requests.get('http://localhost:3000/hotelUuidKey').text
    return hotelUuidKey

conn = None

def get_connection():
    global conn
    if conn is None:
        database_url = "http://192.168.230.130:8765/"
        conn = phoenixdb.connect(database_url, autocommit=True)
        print("new connection")
    return conn