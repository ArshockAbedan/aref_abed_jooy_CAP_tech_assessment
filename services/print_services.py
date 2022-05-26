def print_header_menu(headers, menu_items):
    """
    This function prints the header and the main menu items.
    :param headers: A dict containing items of header section in config file.
    :param menu_items: A dict containing items of menu section in config file.
    :return: None
    """
    print("\n\n\n")
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


def print_customers_balance(deposits, withdrawals):
    """
    This function prints expected output for Task 1.
    :param deposits: A dictionary containing the content of deposits file.
    :param withdrawals: A dictionary containing the content of withdrawals file.
    :return is_finished: if True: program should be finished,
                         if False: we need to show main menu again.
    """
    return False
