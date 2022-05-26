from services import file_services, print_services


def perform_task_1(deposits, withdrawals, task_1_config):
    """
    This function perform Task 1.
    :param deposits: A dictionary containing the content of deposits file.
    :param withdrawals: A dictionary containing the content of withdrawals file.
    :param task_1_config: A dict containing Items of task_1 section of config file.
    :return is_finished: if True: program should be finished,
                         if False: we need to show main menu again.
    """
    print_services.print_customers_balance(deposits, withdrawals, task_1_config)
    return print_services.print_are_you_done()


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

    while True:
        selected_choice = input(config['user_input']['question_text'])
        if selected_choice == "1":
            # user wants to perform task 1
            task_1_config_dict = config['task_1']
            is_finished = perform_task_1(deposits, withdrawals, task_1_config_dict)
            # After performing task 1, is_finished tells us if user want to exit or not
            if is_finished:
                break
            else:
                print_services.print_header_menu(header_dict, menu_dict)
                continue
        elif selected_choice == "2":
            print(f'selected choice is {selected_choice}')
        elif selected_choice == "3":
            print(f'selected choice is {selected_choice}')
        elif selected_choice == "E" or selected_choice == "e":
            print("\nThank you for using this application.")
            break
        else:
            print(f'\nYou entered: {selected_choice}')
            print_services.print_alerts(config['wrong_input'])
            print()


if __name__ == '__main__':
    main()
    exit(0)
