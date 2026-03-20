import pytest
import json


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="prod",
        help="choose environment: test or prod"
    )


def set_environment(config):

    with open(r"C:\Users\ACER\Documents\api_test\environment.json", "r+") as json_file:

        data = json.load(json_file)

        json_file.seek(0)

        data["environment"]["env"] = config.getoption("env").lower()

        json.dump(data, json_file, indent=4)

        json_file.truncate()


@pytest.hookimpl
def pytest_configure(config):
    set_environment(config)