from datetime import datetime
from decimal import Decimal

import pytest

from services.financial_services import calc_over_drafted_customers, \
    calc_highest_total_spender_per_category, \
    delete_outdated_transactions, calc_customers_balance, get_unique_customers, \
    get_total_amount_for_spender_per_category, get_unique_spenders_by_category, get_unique_categories, \
    get_all_transactions_per_customer, get_previous_month_balance


@pytest.fixture()
def my_deposits():
    return [
        {
            "amount": "828.41",
            "customerName": "Glen M. Skipper",
            "time": "2017-12-01 08:00:00"
        },
        {
            "amount": "210.00",
            "customerName": "Michael P. Taylor",
            "time": "2017-11-21 11:00:00"
        },
        {
            "amount": "249.78",
            "customerName": "Abhay Ganymede",
            "time": "2017-12-01 14:00:00"
        },
        {
            "amount": "580.2",
            "customerName": "Issy Anah",
            "time": "2017-12-01 16:00:00"
        },
        {
            "amount": "390.18",
            "customerName": "David E. Hendricks",
            "time": "2017-12-02 00:00:00"
        },
        {
            "amount": "589.44",
            "customerName": "Sophie Olga",
            "time": "2017-12-02 01:00:00"
        },
        {
            "amount": "142.22",
            "customerName": "Michael P. Taylor",
            "time": "2017-12-02 06:00:00"
        }]


@pytest.fixture()
def my_withdrawals():
    return [
        {
            "amount": "879.17",
            "category": "Debit Payment",
            "customerName": "Glen M. Skipper",
            "time": "2017-12-01 20:00:00"
        },
        {
            "amount": "100.13",
            "category": "Debit Payment",
            "customerName": "Glen M. Skipper",
            "time": "2017-12-07 02:20:00"
        },
        {
            "amount": "445.17",
            "category": "Bill",
            "customerName": "Sophie Olga",
            "time": "2017-12-02 12:00:00"
        },
        {
            "amount": "179.31",
            "category": "Debit Payment",
            "customerName": "Abhay Ganymede",
            "time": "2017-12-02 23:00:00"
        },
        {
            "amount": "104.28",
            "category": "ATM",
            "customerName": "Sophie Olga",
            "time": "2017-12-03 00:00:00"
        },
        {
            "amount": "412.27",
            "category": "ATM",
            "customerName": "Michael P. Taylor",
            "time": "2017-12-03 11:00:00"
        }]


def test_calc_customers_balance(my_withdrawals, my_deposits):
    with pytest.raises(TypeError):
        assert calc_customers_balance()
    output = {'Abhay Ganymede': Decimal('70.47'),
              'David E. Hendricks': Decimal('390.18'),
              'Glen M. Skipper': Decimal('-150.89'),
              'Issy Anah': Decimal('580.2'),
              'Michael P. Taylor': Decimal('-60.05'),
              'Sophie Olga': Decimal('39.99')}
    assert calc_customers_balance(withdrawals=my_withdrawals,
                                  deposits=my_deposits) == output


def test_get_unique_customers(my_deposits, my_withdrawals):
    output_withdrawals = {'Abhay Ganymede', 'David E. Hendricks',
                          'Glen M. Skipper', 'Issy Anah', 'Michael P. Taylor',
                          'Sophie Olga'}
    assert get_unique_customers(my_deposits,
                                my_withdrawals) == output_withdrawals


def test_delete_outdated_transactions(my_deposits):
    assert delete_outdated_transactions(my_deposits, 11, 2017) == {}


def test_calc_highest_total_spender_per_category(my_withdrawals):
    output = {'Bill': ['Sophie Olga', Decimal('445.17')],
              'ATM': ['Michael P. Taylor', Decimal('412.27')],
              'Debit Payment': ['Glen M. Skipper', Decimal('979.30')]}
    assert calc_highest_total_spender_per_category(my_withdrawals, 12, 2017) == output
    output = {'ATM': ['Michael P. Taylor', Decimal('412.27')],
              'Bill': ['Sophie Olga', Decimal('445.17')],
              'Debit Payment': ['Glen M. Skipper', Decimal('979.30')]}
    assert calc_highest_total_spender_per_category(my_withdrawals, 11, 2017) == {}


def test_get_total_amount_for_spender_per_category(my_withdrawals):
    category = 'Bill'
    customer = 'Sophie Olga'
    output = Decimal('445.17')
    assert get_total_amount_for_spender_per_category(withdrawals=my_withdrawals,
                                                     needed_category=category,
                                                     spender=customer) == output


def test_get_unique_spenders_by_category(my_withdrawals):
    category = 'Debit Payment'
    output = {'Glen M. Skipper', 'Abhay Ganymede'}
    assert get_unique_spenders_by_category(withdrawals=my_withdrawals,
                                           needed_category=category) == output


def test_get_unique_categories(my_withdrawals):
    output = {'Debit Payment', 'Bill', 'ATM'}
    assert get_unique_categories(withdrawals=my_withdrawals) == output


def test_get_all_transactions_per_customer(my_deposits, my_withdrawals):
    customer_name = "Glen M. Skipper"
    output_list = [(datetime(2017, 12, 1, 8, 0),
                    [Decimal('828.41'), 'deposit', '2017-12-01 08:00:00']),
                   (datetime(2017, 12, 1, 20, 0),
                    [Decimal('879.17'), 'withdrawal', '2017-12-01 20:00:00']),
                   (datetime(2017, 12, 7, 2, 20),
                    [Decimal('100.13'), 'withdrawal', '2017-12-07 02:20:00'])]
    assert get_all_transactions_per_customer(my_deposits,
                                             my_withdrawals,
                                             customer_name) == output_list


def test_delete_outdated_transactions(my_deposits):
    output = [{'amount': '210.00',
               'customerName': 'Michael P. Taylor',
               'time': '2017-11-21 11:00:00'}]
    assert delete_outdated_transactions(my_deposits, 11, 2017) == output


def test_calc_over_drafted_customers(my_deposits, my_withdrawals):
    output = {'Glen M. Skipper': ['2017-12-07 02:20:00', Decimal('-150.89')],
              'Michael P. Taylor': ['2017-12-03 11:00:00', Decimal('-60.05')]}
    assert calc_over_drafted_customers(my_deposits, my_withdrawals, 12, 2017) == output
    empty_output = {}
    assert calc_over_drafted_customers(my_deposits,
                                       my_withdrawals,
                                       requested_month=11,
                                       requested_year=2017) == empty_output


def test_get_previous_month_balance():
    assert get_previous_month_balance("anyone") == 0.00
