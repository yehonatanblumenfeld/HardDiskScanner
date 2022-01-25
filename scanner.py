import os
from printer import write_to_console
from analysis import analyze_file
from data_layer import add_file

import logger
files = []


def scan_hard_disk(hard_disk_letter, file_extension, customer_id):
    try:
        for directory_path, directory_names, filenames in os.walk(f"{hard_disk_letter}:"):
            write_to_console("---------------------------------------------------------")
            write_to_console(f'Correct Path: {directory_path}')
            write_to_console(f'Directories: {directory_names}')
            write_to_console(f'Files: {filenames}')

            if file_extension == "all":
                for filename in filenames:
                    path_for_file = create_path(directory_path, filename)
                    file_attributes = analyze_file(path_for_file, filename, customer_id)
                    add_file(file_attributes)
                    files.append(filename)
            else:
                for filename in filenames:
                    if filename.endswith(file_extension):
                        path_for_file = create_path(directory_path, filename)
                        file_attributes = analyze_file(path_for_file, filename, customer_id)
                        add_file(file_attributes)
                        files.append(filename)
                        continue

        write_to_console(f"there are {len(files)} files of the '{file_extension}' extension")
        logger.log_message("all files has been scanned")
    except:
        logger.log_message("error occured while scannig the path")


def create_path(path: str, filename: str):
    try:
        return os.path.join(path, filename)
    except:
        logger.log_message("error occured while creating the path in scan_hard_disk function")
