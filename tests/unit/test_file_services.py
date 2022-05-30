import pytest

from services import file_services


def test_read_config():
    my_config = file_services.read_config(file_services.CONFIG_FILE)
    assert len(my_config.sections()) > 0, f"The {file_services.CONFIG_FILE} file is empty."
    assert my_config.has_section("files_path")
    assert my_config.has_option("files_path", "deposits")
    assert my_config.has_option("files_path", "withdrawals")
    assert my_config.has_section("header")
    assert my_config.has_section("menu")
    assert len(my_config['menu'].items()) == 4
    assert len(my_config['menu'].items()) == len(my_config['menu_accepted_options'].items())
    assert my_config.has_section("user_input")
    assert my_config.has_option("user_input", "question_text")
    assert my_config.has_section("wrong_input")
    assert my_config.has_option("wrong_input", "alert_1")
    assert my_config.has_option("wrong_input", "alert_2")
    assert my_config.has_section("task_1")
    assert my_config.has_option("task_1", "result_title")
    assert my_config.has_option("task_1", "sorted")
    assert my_config.has_option("task_1", "descending")
    assert my_config.has_option("task_1", "customer_col_title")
    assert my_config.has_option("task_1", "customer_col_size")
    assert my_config.has_option("task_1", "balance_col_title")
    assert my_config.has_option("task_1", "balance_col_size")
    assert my_config.has_option("task_1", "adjuster")
    assert my_config.has_section("task_2")
    assert my_config.has_option("task_2", "requested_month")
    assert my_config.has_option("task_2", "result_title")
    assert my_config.has_option("task_2", "final_msg_per_category")
    assert my_config.has_section("task_3")
    assert my_config.has_option("task_3", "requested_month")
    assert my_config.has_option("task_3", "result_title")
    assert my_config.has_option("task_3", "final_msg_per_customer")
    assert my_config.has_section("are_you_done")
    assert my_config.has_option("are_you_done", "question_title")
    assert my_config.has_option("are_you_done", "user_input_title")
    assert my_config.has_option("are_you_done", "accepted_options")


def test_read_json_file():
    with pytest.raises(OSError):
        file_services.read_json_file("")
