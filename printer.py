# is only job is to print the message
import json


def write_to_console(message):
    print(message)


def write_file_list_to_console(list):
    if len(list) == 0:
        print("there are no hidden files")
        return

    print("------------------------------ [Files list] ----------------------------------")
    for ele in list:
        # ele = json.load(ele)
        print(f'___________{ele["file_name"]}___________')
        print(f'File extension: {ele["file_extension"]}')
        print(f'Is hidden: {ele["is_hidden"]}')
        print(f'Creation time: {ele["creation_time"]}')
