import configparser
import json
import os

# Find base directory of project in OS
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Actual path of the configuration file i.e. config.ini
CONFIG_FILE = os.path.join(BASE_DIR, 'config.ini')


def read_config(conf):
    """
    This function reads the config file.
    :param conf: Path of configuration file i.e. CONFIG_FILE
    :return: config: A dictionary containing the content of config file
    """
    try:
        config = configparser.ConfigParser()
        config.read(conf)
    except KeyError as err:
        print(err)
        print(f'The {conf} is not valid.')
    return config


def read_json_file(file_path):
    """
    This function reads a json file
    :param file_path: The path of json file
    :return: A dictionary containing the content of read file
    """
    file_contents = {}  # this dict will be returned.
    try:
        with open(file_path, 'r') as data_file:
            file_contents = json.load(data_file)
    except IOError as error:
        print(error)
        print("IOError error: unable to open ", file_path, ". Terminating execution.")
    finally:
        data_file.close()
    return file_contents
