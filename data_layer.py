from printer import write_to_console
import connection
from pymongo import MongoClient
import logger

cluster = MongoClient(connection.connection_string)
db = cluster["FileAnalayzer"]
collection = db["files"]


def add_file(analyzed_file):
    try:
        collection.insert_one(analyzed_file)
    except:
        logger.log_message("error occured while adding a file to the database")


def get_hidden_files():
    try:
        return list(collection.find({"is_hidden": True}))
    except:
        logger.log_message("error occured while trying to get files from the database")
