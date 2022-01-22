import os
from datetime import datetime
from printer import write_to_console
from hashlib import sha256
import win32api
import win32con
import logger


# This function get the path and the name of the file and extract the values needed
def analyze_file(path: str, file_name: str, customer_id):
    try:
        file_data = os.stat(path)

        # extracting file extension
        file_extension = "." + file_name.split(".", 1)[1]
        # extracting file isHidden
        attribute = win32api.GetFileAttributes(path)
        hidden = attribute & (win32con.FILE_ATTRIBUTE_HIDDEN | win32con.FILE_ATTRIBUTE_SYSTEM)
        is_file_hidden = False
        if hidden == 2:
            is_file_hidden = True

        # extracting creation time
        creation_time = datetime.fromtimestamp(file_data.st_ctime)
        file_creation_time = creation_time.strftime("%d/%m/%y in %H:%M:%S")

        # getting tha data in sha256
        file_sha256 = str(sha256(str(file_data).encode()))

        # creating an object with the values extracted
        file_attributes = \
            {"customer_id": customer_id,
                "file_name": file_name,
                "file_extension": file_extension,
                "is_hidden": is_file_hidden,
                "creation_time": file_creation_time,
                "sha256": file_sha256}

        return file_attributes

    except:
        logger.log_message("error occured while analyzing the file")
