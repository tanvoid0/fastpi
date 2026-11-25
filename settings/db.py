# Initialize Database
from decouple import config
from mongoengine import connect, disconnect
from pymongo import MongoClient


def db_connect():
    print("DB Connecting...")
    connect(
        host=host,
    )
    print("DB Connected successfully")


def db_disconnect():
    disconnect()
    print("DB Disconnected")


host = config("DB_HOST")
client = MongoClient(host)
db = client['api']
