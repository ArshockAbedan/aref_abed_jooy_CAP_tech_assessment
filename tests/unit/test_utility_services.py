import pytest

from services import utility_services


def test_sort_dict_by_value():
    with pytest.raises(TypeError):
        assert utility_services.sort_dict_by_value()
