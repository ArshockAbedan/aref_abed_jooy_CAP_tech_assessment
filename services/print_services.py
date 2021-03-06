"""
@File    :   print_services.py
@Contact :   arefabedjooy@gmail.com
@License :   (C)Copyright 2020-2022

@Modify Time          @Author        @Version      @Description
-----------------   ------------     --------    --------------------
5/25/2022 8:07 PM  Aref Abedjooy      1.0       Services related to print outputs
"""

from services import financial_services
from services import utility_services


def print_header_menu(headers, menu_items):
    """
    This function prints the header and the main menu items.
    :param headers: A dict containing items of header section in config file.
    :param menu_items: A dict containing items of menu section in config file.
    :return: None
    """
    print_header(headers)
    print_menu(menu_items)


def print_header(headers):
    """
    This function prints Header part of main menu.
    :param headers: A dict containing items of header section in config file.
    :return: None
    """
    for header_txt in headers.values():
        print(header_txt)


def print_menu(menu_items):
    """
    This function prints the header and the main menu items.
    :param menu_items: A dict containing items of menu section in config file.
    :return: None
    """
    for menu_item in menu_items.values():
        print(menu_item)
        print()


def print_alerts(alerts):
    """
    This function prints alerts after user's incorrect input.
    :param alerts: A dict containing items of wrong_input section i.e. alerts in config file.
    :return: None
    """
    for alert in alerts.values():
        print(alert)


def print_table_divider(first_col_size, second_col_size, adjuster):
    """
    This functions print a vertical divider.
    :param first_col_size: size of first column.
    :param second_col_size: size of second column.
    :param adjuster: add extra needed '-' to fill space.
    :return: None
    """
    print("|", end="")
    for _ in range(first_col_size + second_col_size + adjuster):
        print("-", end="")
    print("|")


def print_are_you_done(config_dict):
    """
     print a question and asking user for if he or she want to exit or not.
    :param config_dict: A dict containing items of are_you_done section of config file.
    :return is_done: a bool determining if user want to exit or not,
                     True means he or she wants to exit.
    """
    print("\n" + config_dict['question_title'])
    user_choice = input(config_dict['user_input_title'])
    accepted_options = str(config_dict['accepted_options']).split(',')
    if user_choice in accepted_options:
        is_done = True
    else:
        is_done = False
    return is_done


def print_customers_balance(deposits, withdrawals, config_dict):
    """
    This function prints expected output for Task 1.
    :param deposits: A list of dictionaries containing the content of deposits file.
    :param withdrawals: A list of dictionaries containing the content of withdrawals file.
    :param config_dict: A dict containing items of task_1 section in config file.
    :return: None
    """
    unique_customers_balance_dict = financial_services.calc_customers_balance(deposits, withdrawals)

    # if the output needs to be sorted, it will be handled here.
    if config_dict['sorted'] == "1":
        if config_dict['descending'] == "1":
            unique_customers_balance_dict = \
                utility_services.sort_dict_by_value(unique_customers_balance_dict, True)
        else:
            unique_customers_balance_dict = \
                utility_services.sort_dict_by_value(unique_customers_balance_dict, False)
    print(config_dict['result_title'])

    customer_col_title = config_dict['customer_col_title']  # title of customer column
    customer_col_size = int(config_dict['customer_col_size'])  # size of customer column
    balance_col_title = config_dict['balance_col_title']  # title of balance Column
    balance_col_size = int(config_dict['balance_col_size'])  # size of balance Column
    adjuster = int(config_dict['adjuster'])  # Adjust extra space in divider

    # print a divider between rows. First of is top of table.
    print_table_divider(customer_col_size, balance_col_size, adjuster)

    # Print headers of columns
    print("|", customer_col_title.ljust(customer_col_size), "|",
          str(balance_col_title).ljust(balance_col_size), "|")

    # A divider below headers of columns
    print_table_divider(customer_col_size, balance_col_size, adjuster)

    # For each unique customer, expected output will be printed.
    for unique_customer_name, unique_customer_balance in unique_customers_balance_dict.items():
        print("|", unique_customer_name.ljust(customer_col_size),
              "|",
              str(unique_customer_balance).ljust(balance_col_size),
              "|")

    # Print a divider below last customer.
    print_table_divider(customer_col_size, balance_col_size, adjuster)


def print_highest_total_spender_per_category(withdrawals, config_dict):
    """
    This function prints expected output for Task 2.
    :param withdrawals: A list of dictionaries containing the content of withdrawals file.
    :param config_dict: A dict containing items of task_2 section in config file.
    :return: None
    """
    requested_month = int(config_dict['requested_month'])
    requested_year = int(config_dict['requested_year'])
    highest_spender_in_each_category_dict = \
        financial_services.calc_highest_total_spender_per_category(withdrawals,
                                                                   requested_month,
                                                                   requested_year)
    print(config_dict['result_title'] + "\n")

    i = 1  # counter for categories
    for category, [customer, amount] in highest_spender_in_each_category_dict.items():
        print(config_dict['final_msg_per_category'].format(str(i), category, customer, str(amount)))
        i += 1


def print_over_drafted_customers(deposits, withdrawals, config_dict):
    """
    This function prints expected output for Task 3.
    :param deposits: A list of dictionaries containing the content of deposits file.
    :param withdrawals: A list of dictionaries containing the content of withdrawals file.
    :param config_dict: A dict containing items of task_3 section in config file.
    :return: None
    """
    requested_month = int(config_dict['requested_month'])
    requested_year = int(config_dict['requested_year'])
    over_drafted_customers_dict = \
        financial_services.calc_over_drafted_customers(deposits,
                                                       withdrawals,
                                                       requested_month,
                                                       requested_year)
    print(config_dict['result_title'] + "\n")

    i = 1  # counter for customer
    for customer, [time, amount] in over_drafted_customers_dict.items():
        print(config_dict['final_msg_per_customer'].format(str(i), customer, str(amount), time))
        i += 1
