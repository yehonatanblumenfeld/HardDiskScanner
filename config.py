import json
from printer import write_to_console


def config_params():
    try:
        # trying to read the config file and get the parameters
        config_file = open("config.json", "rt")
        params = json.loads(config_file.read())
        return params

    except:
        # in here if there is no file to read from
        write_to_console("file was not found")

        # creating a new object with the needed parameters
        parameters = {"fileExtension": ".exe", "hardDisk": "F", "customerId": "1234"}

        # creating a new config file and writing the necessary data into it
        config_file = open("config.json", "a")
        config_file.write(json.dumps(parameters))
        config_file.close()
        params = parameters
        return params
