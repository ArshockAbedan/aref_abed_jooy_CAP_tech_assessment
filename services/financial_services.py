"""
@File    :   financial_services.py
@Contact :   arefabedjooy@gmail.com
@License :   (C)Copyright 2020-2022

@Modify Time          @Author        @Version      @Description
-----------------   ------------     --------    --------------------
5/26/2022 10:27 AM  Aref Abedjooy      1.0       Services related to financial calculations
"""

import decimal


def get_previous_month_balance(customer):
    """
    This function returns the balance of previous month for the customer.
    :param customer: Name of customer
    :return previous_balance: the balance of previous month for the customer.
    """
    # for the simplification, it is assumed that all previous balance are zero.
    previous_balance = decimal.Decimal(0.00)
    return previous_balance


def calc_customers_balance(deposits, withdrawals):
    """
    This function calculate expected output for task 1.
    :param deposits: A list of dictionaries containing the content of deposits file.
    :param withdrawals: A list of dictionaries containing the content of withdrawals file.
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


def get_unique_categories(withdrawals):
    """
    This function returns unique categories in withdrawals JSON file.
    :param withdrawals: A list of dictionaries containing the content of withdrawals file.
    :return unique_categories: a set containing  all unique categories.
    """
    unique_categories = set()
    for withdrawal in withdrawals:
        category = withdrawal['category']
        unique_categories.add(category)
    return unique_categories


def get_unique_customers(withdrawals):
    """
    This function returns unique customers in withdrawals JSON file.
    :param withdrawals: A list of dictionaries containing the content of withdrawals file.
    :return unique_customers: a set containing  all unique customers.
    """
    unique_customers = set()
    for withdrawal in withdrawals:
        customer_name = withdrawal['customerName']
        unique_customers.add(customer_name)
    return unique_customers


def get_unique_customers_by_category(withdrawals, needed_category):
    """
    This function returns unique customers for a category in withdrawals JSON file.
    :param withdrawals: A list of dictionaries containing the content of withdrawals file.
    :param needed_category: A category.
    :return unique_customers: a set containing  all unique customers for this category.
    """
    unique_customers = set()
    for withdrawal in withdrawals:
        customer_name = withdrawal['customerName']
        category = withdrawal['category']
        if category == needed_category:
            unique_customers.add(customer_name)
    return unique_customers


def get_total_amount_for_spender_per_category(withdrawals, needed_category, spender):
    """
        This function returns total amount that a spender spends in needed_category in withdrawals JSON file.
        :param withdrawals: A list of dictionaries containing the content of withdrawals file.
        :param needed_category: A category.
        :param spender: A customer.
        :return total_amount: total amount that a spender spends in the needed_category.
    """
    total_amount = decimal.Decimal(0.00)
    for withdrawal in withdrawals:
        customer_name = withdrawal['customerName']
        category = withdrawal['category']
        amount = decimal.Decimal(withdrawal['amount'])
        if category == needed_category and customer_name == spender:
            total_amount += amount
    return total_amount


def calc_highest_total_spender_per_category(withdrawals):
    """
    This function calculate expected output for task 2.
    :param withdrawals: A list of dictionaries containing the content of withdrawals file.
    :return highest_spender_in_each_category_dict: a dictionary containing  highest total spender
                                                   in each payment category.
    """
    highest_spender_in_each_category_dict = {}  # {'Category': ['customer_name', Decimal('amount')]}
    unique_categories_set = get_unique_categories(withdrawals)
    for category in unique_categories_set:
        unique_customers_set = get_unique_customers_by_category(withdrawals, category)
        highest_total_amount = decimal.Decimal(0.00)
        spender_with_highest_amount = ""
        for customer in unique_customers_set:
            sum_amount = \
                get_total_amount_for_spender_per_category(withdrawals, category, customer)
            if sum_amount > highest_total_amount:
                highest_total_amount = sum_amount
                spender_with_highest_amount = customer
        highest_spender_in_each_category_dict[category] = \
            [spender_with_highest_amount, highest_total_amount]
    return highest_spender_in_each_category_dict
