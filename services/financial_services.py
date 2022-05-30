"""
@File    :   financial_services.py
@Contact :   arefabedjooy@gmail.com
@License :   (C)Copyright 2020-2022

@Modify Time          @Author        @Version      @Description
-----------------   ------------     --------    --------------------
5/26/2022 10:27 AM  Aref Abedjooy      1.0       Services related to financial calculations
"""

import decimal
from datetime import datetime

from services import utility_services

DECIMAL_ZERO = decimal.Decimal(0.00)


def get_previous_month_balance(customer):
    """
    This function returns the balance of previous month for the customer.
    :param customer: Name of customer
    :return previous_balance: the balance of previous month for the customer.
    """
    # for the simplification, it is assumed that all previous balances are zero.
    previous_balance = DECIMAL_ZERO
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

    # Here we are considering all transactions. There is no preprocessing here.

    for deposit in deposits:
        customer_name = deposit['customerName']
        amount = decimal.Decimal(deposit['amount'])
        if customer_name in unique_customers:
            unique_customers[customer_name] += amount
        else:
            unique_customers[customer_name] = get_previous_month_balance(customer_name) + amount

    for withdrawal in withdrawals:
        customer_name = withdrawal['customerName']
        amount = decimal.Decimal(withdrawal['amount'])
        if customer_name in unique_customers:
            unique_customers[customer_name] -= amount
        else:
            unique_customers[customer_name] = get_previous_month_balance(customer_name) - amount

    return unique_customers


def delete_outdated_transactions(transactions_dict, month_int):
    """
    This function deletes transactions that are not in 'month_int' month.
    :param transactions_dict: A list of dictionaries containing
                              the content of either deposits or withdrawals JSON files.
    :param month_int: An integer representing a month.
    :return transactions_dict: A list of dictionaries containing
                               all transactions within just 'month_int' month.
    """
    to_be_deleted_transactions = []
    for transaction in transactions_dict:
        time = datetime.fromisoformat(transaction['time'])
        if time.month != month_int:
            to_be_deleted_transactions.append(transaction)

    for to_be_deleted_transaction in to_be_deleted_transactions:
        transactions_dict.remove(to_be_deleted_transaction)
    return transactions_dict


def get_unique_customers(deposits, withdrawals):
    """
    This function returns unique customers in withdrawals JSON file.
    :param deposits: A list of dictionaries containing the content of deposits file.
    :param withdrawals: A list of dictionaries containing the content of withdrawals file.
    :return unique_customers: a set containing  all unique customers.
    """
    unique_customers = set()
    for withdrawal in withdrawals:
        customer_name = withdrawal['customerName']
        unique_customers.add(customer_name)
    for deposit in deposits:
        customer_name = deposit['customerName']
        unique_customers.add(customer_name)
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


def get_unique_spenders_by_category(withdrawals, needed_category):
    """
    This function returns unique customers for a category in withdrawals JSON file.
    :param withdrawals: A list of dictionaries containing the content of withdrawals file.
    :param needed_category: A category.
    :return unique_customers: a set containing  all unique customers for this category.
    """
    unique_spenders = set()
    for withdrawal in withdrawals:
        customer_name = withdrawal['customerName']
        category = withdrawal['category']
        if category == needed_category:
            unique_spenders.add(customer_name)
    return unique_spenders


def get_total_amount_for_spender_per_category(withdrawals, needed_category, spender):
    """
    This function returns total amount that a spender spends in needed_category in withdrawals JSON file.
    :param withdrawals: A list of dictionaries containing the content of withdrawals file.
    :param needed_category: A category.
    :param spender: A customer.
    :return total_amount: total amount that a spender spends in the needed_category.
    """
    total_amount = DECIMAL_ZERO
    for withdrawal in withdrawals:
        customer_name = withdrawal['customerName']
        category = withdrawal['category']
        amount = decimal.Decimal(withdrawal['amount'])
        if category == needed_category and customer_name == spender:
            total_amount += amount
    return total_amount


def calc_highest_total_spender_per_category(withdrawals, *args, **kwargs):
    """
    This function calculate expected output for task 2.
    :param withdrawals: A list of dictionaries containing the content of withdrawals file.
    :param args: requested_month: number of month which its transactions are needed only.
    :return highest_spender_in_each_category_dict: a dictionary containing  highest total spender
                                                   in each payment category.
    """
    highest_spender_in_each_category_dict = {}  # {'Category': ['customer_name', Decimal('amount')]}

    requested_month = kwargs.get('requested_month', None)

    # requested_month = 0 means all months are needed.
    if requested_month == 0:
        requested_month = None

    if requested_month:
        # Prepossessing - Delete transactions that are outdated.
        withdrawals = delete_outdated_transactions(withdrawals, requested_month)

    unique_categories_set = get_unique_categories(withdrawals)

    for category in unique_categories_set:
        unique_customers_set = get_unique_spenders_by_category(withdrawals, category)
        highest_total_amount = DECIMAL_ZERO
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


def get_all_transactions_per_customer(deposits, withdrawals, customer):
    """
    This function calculate expected output for task 3.
    :param deposits: A list of dictionaries containing the content of deposits file.
    :param withdrawals: A list of dictionaries containing the content of withdrawals file.
    :param customer: A customer.
    :return customer_transactions_sorted_list: a list containing all of customer's transactions
                                               each of its item has 2 items;
                                               first: transaction_time, second: transaction_details
    """
    customer_transactions = {}

    for withdrawal in withdrawals:
        customer_name = withdrawal['customerName']
        amount = decimal.Decimal(withdrawal['amount'])
        time_str = withdrawal['time']
        time = datetime.fromisoformat(withdrawal['time'])
        if customer_name == customer:
            customer_transactions[time] = [amount, "withdrawal", time_str]

    for deposit in deposits:
        customer_name = deposit['customerName']
        amount = decimal.Decimal(deposit['amount'])
        time_str = deposit['time']
        time = datetime.fromisoformat(deposit['time'])
        if customer_name == customer:
            customer_transactions[time] = [amount, "deposit", time_str]

    # sort all transactions in chronological order
    customer_transactions_sorted_list = sorted(customer_transactions.items(), reverse=False)
    return customer_transactions_sorted_list


def calc_over_drafted_customers(deposits, withdrawals, *args, **kwargs):
    """
    This function calculate expected output for task 3.
    :param deposits: A list of dictionaries containing the content of deposits file.
    :param withdrawals: A list of dictionaries containing the content of withdrawals file.
    :param args: requested_month: number of month which its transactions are needed only.
    :return over_drafted_customers: a dictionary containing  all customers,
                              who over drafted their account at any point in the month of December.
    """
    over_drafted_customers = {}

    requested_month = kwargs.get('requested_month', None)

    # requested_month = 0 means all months are needed.
    if requested_month == 0:
        requested_month = None

    if requested_month:
        # Prepossessing - Delete transactions that are outdated.
        deposits = delete_outdated_transactions(deposits, requested_month)
        withdrawals = delete_outdated_transactions(withdrawals, requested_month)

    unique_customers = get_unique_customers(deposits, withdrawals)
    for customer in unique_customers:
        customer_transactions = get_all_transactions_per_customer(deposits, withdrawals, customer)
        customer_total_balance = DECIMAL_ZERO
        customer_max_over_drafted_balance = DECIMAL_ZERO
        customer_max_over_drafted_time = ""
        for transaction_time, transaction_details in customer_transactions:
            transaction_amount = transaction_details[0]
            transaction_type = transaction_details[1]  # "withdrawal" or "deposit"
            transaction_time_str = transaction_details[2]  # time (string)
            if transaction_type == "deposit":
                customer_total_balance += transaction_amount
            else:
                # it means transaction_type == "withdrawal"
                customer_total_balance -= transaction_amount

            if customer_total_balance < DECIMAL_ZERO:
                # more negative value means max
                if customer_total_balance < customer_max_over_drafted_balance:
                    customer_max_over_drafted_balance = customer_total_balance
                    customer_max_over_drafted_time = transaction_time_str

        if customer_max_over_drafted_balance < DECIMAL_ZERO:
            over_drafted_customers[customer] = \
                [customer_max_over_drafted_time, customer_max_over_drafted_balance]

    return over_drafted_customers
