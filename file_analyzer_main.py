from config import config_params
from concurrent.futures import ThreadPoolExecutor
from scanner import scan_hard_disk
from data_layer import get_hidden_files
from printer import write_file_list_to_console
import logger


def main():
    # getting the data from the config file
    with ThreadPoolExecutor(max_workers=2) as executor:
        params = executor.submit(config_params)
        my_params = params.result()
        scan = executor.submit(scan_hard_disk(my_params["hardDisk"], my_params["fileExtension"],  my_params["customerId"]))

    write_file_list_to_console(get_hidden_files())
    logger.log_message("scanning completed")


if __name__ == "__main__":
    main()
