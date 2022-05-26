import pytest

from services import print_services


def test_print_header_menu():
    with pytest.raises(TypeError):
        assert print_services.print_header_menu()


def test_print_header():
    with pytest.raises(TypeError):
        assert print_services.print_header()


def test_print_menu():
    with pytest.raises(TypeError):
        assert print_services.print_menu()


def test_print_alerts():
    with pytest.raises(TypeError):
        assert print_services.print_alerts()


def test_print_table_divider():
    with pytest.raises(TypeError):
        assert print_services.print_table_divider("1", "2", "3")


def test_print_customers_balance():
    dict = {}
    with pytest.raises(TypeError):
        assert print_services.print_customers_balance(dict)
