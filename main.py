from services import file_services, print_services


def main():
    # Read the config file.
    config = file_services.read_config(file_services.CONFIG_FILE)

    # Check if config file is empty or not
    if len(config.sections()) > 0:
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
                is_finished = print_services.print_customers_balance(deposits, withdrawals)
                if is_finished:
                    break
                else:
                    print_services.print_header_menu(header_dict, menu_dict)
                    continue
                print(f'selected choice is {selected_choice}')
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
    else:
        # The config file is empty.
        print(f'The {file_services.CONFIG_FILE} file is empty.')


if __name__ == '__main__':
    main()
    exit(0)
