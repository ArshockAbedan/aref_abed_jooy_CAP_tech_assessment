"""
@File    :   financial_services.py
@Contact :   arefabedjooy@gmail.com
@License :   (C)Copyright 2020-2022

@Modify Time          @Author        @Version      @Description
-----------------   ------------     --------    --------------------
5/26/2022 10:27 AM  Aref Abedjooy      1.0       Services related to financial calculations
"""

import decimal


def get_previous_month_balance(customer_name):
    """
    This function returns the balance of previous month for the customer.
    :param customer_name: Name of customer
    :return previous_balance: the balance of previous month for the customer.
    """
    # for the simplification, it is assumed that all previous balance are zero.
    previous_balance = decimal.Decimal(0.00)
    return previous_balance


def calc_customers_balance(deposits, withdrawals):
    """
    This function calculate expected output for task 1.
    :param deposits: A dictionary containing the content of deposits file.
    :param withdrawals: A dictionary containing the content of withdrawals file.
    :return unique_customers: a dictionary containing  all customers who hold a savings account
                              at this bank, and their final account balances at the end of the month.
    """
    unique_customers = {}
    for deposit in deposits:
        customer_name = deposit['customerName']
        amount = decimal.Decimal(deposit['amount'], )
        time = deposit['time']
        if customer_name in unique_customers:
            unique_customers[customer_name] += amount
        else:
            unique_customers[customer_name] = get_previous_month_balance(customer_name) + amount

    for withdrawal in withdrawals:
        customer_name = withdrawal['customerName']
        amount = decimal.Decimal(withdrawal['amount'])
        category = withdrawal['category']
        time = withdrawal['time']
        if customer_name in unique_customers:
            unique_customers[customer_name] -= amount
        else:
            unique_customers[customer_name] = get_previous_month_balance(customer_name) - amount
    return unique_customers


def calc_highest_total_spender_per_category(withdrawals):
    """
    This function calculate expected output for task 2.
    :param withdrawals: A dictionary containing the content of withdrawals file.
    :return highest_spender_in_each_category_dict: a dictionary containing  all customers who hold
                                               a savings account at this bank,
                                               and their final account balances at the end of the month.
    """
    highest_spender_in_each_category_dict = {}  # {'Category': ['customer_name', Decimal('amount')]}
    for withdrawal in withdrawals:
        customer_name = withdrawal['customerName']
        amount = decimal.Decimal(withdrawal['amount'])
        category = withdrawal['category']
        if category in highest_spender_in_each_category_dict:
            if amount > highest_spender_in_each_category_dict[category][1]:
                highest_spender_in_each_category_dict[category] = [customer_name, amount]
        else:
            highest_spender_in_each_category_dict[category] = [customer_name, amount]
    return highest_spender_in_each_category_dict
