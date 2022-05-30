"""
@File    :   main.py
@Contact :   arefabedjooy@gmail.com
@License :   (C)Copyright 2020-2022

@Modify Time          @Author        @Version      @Description
-----------------   ------------     --------    --------------------
5/24/2022 9:04 PM   Aref Abedjooy      1.0       program start point
"""
from services import file_services, print_services


def perform_task_1(deposits, withdrawals, task_1_config, are_you_done_config_dict):
    """
    This function performs Task 1.
    :param deposits: A list of dictionaries containing the content of deposits file.
    :param withdrawals: A list of dictionaries containing the content of withdrawals file.
    :param task_1_config: A dict containing items of task_1 section of config file.
    :param are_you_done_config_dict: A dict containing items of are_you_done section of config file.
    :return is_finished: if True: program should be finished,
                         if False: we need to show main menu again.
    """
    print_services.print_customers_balance(deposits, withdrawals, task_1_config)
    is_finished = print_services.print_are_you_done(are_you_done_config_dict)
    return is_finished


def perform_task_2(withdrawals, task_2_config, are_you_done_config_dict):
    """
     This function performs Task 2.
    :param withdrawals: A list of dictionaries containing the content of withdrawals file.
    :param task_2_config: A dict containing items of task_2 section of config file.
    :param are_you_done_config_dict: A dict containing items of are_you_done section of config file.
    :return is_finished: if True: program should be finished,
                         if False: we need to show main menu again.
    """
    print_services.print_highest_total_spender_per_category(withdrawals, task_2_config)
    is_finished = print_services.print_are_you_done(are_you_done_config_dict)
    return is_finished


def perform_task_3(deposits, withdrawals, task_3_config, are_you_done_config_dict):
    """
     This function performs Task 3.
    :param deposits: A list of dictionaries containing the content of deposits file.
    :param withdrawals: A list of dictionaries containing the content of withdrawals file.
    :param task_3_config: A dict containing items of task_3 section of config file.
    :param are_you_done_config_dict: A dict containing items of are_you_done section of config file.
    :return is_finished: if True: program should be finished,
                         if False: we need to show main menu again.
    """
    print_services.print_over_drafted_customers(deposits, withdrawals, task_3_config)
    is_finished = print_services.print_are_you_done(are_you_done_config_dict)
    return is_finished


def main():
    # Read the config file.
    config = file_services.read_config(file_services.CONFIG_FILE)

    # Read deposits JSON file.
    deposits_file_path = config['files_path']['deposits']
    deposits = file_services.read_json_file(deposits_file_path)

    # Read withdrawals JSON file.
    withdrawals_file_path = config['files_path']['withdrawals']
    withdrawals = file_services.read_json_file(withdrawals_file_path)

    # print Header and Main Menu items.
    header_dict = config['header']
    menu_dict = config['menu']
    print_services.print_header_menu(header_dict, menu_dict)
    menu_accepted_options_dict = config['menu_accepted_options']

    while True:
        selected_choice = input(config['user_input']['question_text'])
        if selected_choice in menu_accepted_options_dict['task_1_accepted'].split(','):
            # user wants to perform task 1
            task_1_config_dict = config['task_1']
            are_you_done_config_dict = config['are_you_done']
            is_finished = perform_task_1(deposits,
                                         withdrawals,
                                         task_1_config_dict,
                                         are_you_done_config_dict)
            # After performing task 1, is_finished tells us if user want to exit or not
            if is_finished:
                break
            else:
                print_services.print_header_menu(header_dict, menu_dict)
                continue
        elif selected_choice in menu_accepted_options_dict['task_2_accepted'].split(','):
            # user wants to perform task 2
            task_2_config_dict = config['task_2']
            are_you_done_config_dict = config['are_you_done']
            is_finished = perform_task_2(withdrawals,
                                         task_2_config_dict,
                                         are_you_done_config_dict)
            # After performing task 2, is_finished tells us if user want to exit or not
            if is_finished:
                break
            else:
                print_services.print_header_menu(header_dict, menu_dict)
                continue
        elif selected_choice in menu_accepted_options_dict['task_3_accepted'].split(','):
            # user wants to perform task 3
            task_3_config_dict = config['task_3']
            are_you_done_config_dict = config['are_you_done']
            is_finished = perform_task_3(deposits,
                                         withdrawals,
                                         task_3_config_dict,
                                         are_you_done_config_dict)
            # After performing task 3, is_finished tells us if user want to exit or not
            if is_finished:
                break
            else:
                print_services.print_header_menu(header_dict, menu_dict)
                continue
        elif selected_choice in menu_accepted_options_dict['exit_accepted'].split(','):
            print("\nThank you for using this application.")
            break
        else:
            print(f'\nYou entered: {selected_choice}')
            print_services.print_alerts(config['wrong_input'])
            print()


if __name__ == '__main__':
    main()
    exit(0)
