import pytest

from services import financial_services


def test_calc_customers_balance():
    with pytest.raises(TypeError):
        assert financial_services.calc_customers_balance()
