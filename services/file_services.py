"""
@File    :   file_services.py
@Contact :   arefabedjooy@gmail.com
@License :   (C)Copyright 2020-2022

@Modify Time          @Author        @Version      @Description
-----------------   ------------     --------    --------------------
5/25/2022 7:54 PM   Aref Abedjooy      1.0       Services related to file
"""

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
    config = configparser.ConfigParser()
    config.read(conf)
    return config


def read_json_file(file_path):
    """
    This function reads a json file
    :param file_path: The path of json file
    :return: A dictionary containing the content of read file
    """
    file_full_path = os.path.join(BASE_DIR, file_path)
    if not os.path.exists(file_full_path):
        raise OSError(f'Unable to open: {file_full_path}')
    with open(file_full_path, 'r') as data_file:
        file_contents = json.load(data_file)
    return file_contents
