import pytest

from services import utility_services


@pytest.fixture()
def my_dict():
    return {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}


def test_sort_dict_by_value(my_dict):
    with pytest.raises(TypeError):
        assert utility_services.sort_dict_by_value()
    dict_out = {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
    dict_out_desc = {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
    assert utility_services.sort_dict_by_value(unsorted_dict=my_dict, reverse=False) == dict_out
    assert utility_services.sort_dict_by_value(unsorted_dict=my_dict, reverse=True) == dict_out_desc

