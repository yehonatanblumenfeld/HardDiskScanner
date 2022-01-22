from datetime import datetime


def log_message(msg: str):
    # trying to open the file if existing , if not creates new one
    logger = open("logger.txt", "a")
    logger.write(f"----------------------message time: {datetime.now()}---------------------\n")
    logger.write(f"===> message: {msg}\n")
    logger.close()


