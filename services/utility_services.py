"""
@File    :   utility_services.py
@Contact :   arefabedjooy@gmail.com
@License :   (C)Copyright 2020-2022

@Modify Time          @Author        @Version      @Description
-----------------   ------------     --------    --------------------
5/26/2022 11:21 AM  Aref Abedjooy      1.0       Services related to utilities
"""


def sort_dict_by_value(unsorted_dict, reverse=False):
    """
    This function sorts the input dictionary.
    :param unsorted_dict: an unsorted plain dictionary.
    :param reverse: A boolean that True as its value means the result would be in descending order.
    :return: a dictionary sorted by its values
    """
    return dict(sorted(unsorted_dict.items(), key=lambda x: x[1], reverse=reverse))


