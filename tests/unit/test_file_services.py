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
    assert my_config.has_section("user_input")
    assert my_config.has_option("user_input", "question_text")
    assert my_config.has_section("wrong_input")
    assert my_config.has_section("task_1")
    assert my_config.has_section("task_2")
    assert my_config.has_section("task_3")


def test_read_json_file():
    with pytest.raises(OSError):
        file_services.read_json_file("")
