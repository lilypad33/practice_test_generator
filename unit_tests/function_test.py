import pytest
import os
from unittest.mock import patch
from test_generator import list_csv_files
from test_generator import select_option

def test_list_csvs_as_list():
    '''
    Checks that the list_csv_files function returns a list
    '''

    example_directory = os.path.join("practice_tests", "AWS")

    directory_list = list_csv_files(example_directory)

    assert isinstance(directory_list, list)


def test_select_option_valid():
    '''
    Ensures the select option function returns a number, which select_option converts from a string into an integer.
    '''
    example_directory = os.path.join("practice_tests", "AWS")

    test_list = list_csv_files(example_directory)


    with patch("builtins.input", return_value = "1"):
        test_value = select_option(test_list)
        assert isinstance(test_value, int)

