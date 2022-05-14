from mongoengine import connect


class Database:
    def __init__(self):
        connect(
            db="api",
            host="mongodb+srv://user-api:srfpKh1e6QH6vfg4@cluster0.jo4do.mongodb.net/api",
            username="user-api",
            password="srfpKh1e6QH6vfg4"
        )
