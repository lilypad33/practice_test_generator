import os
import pytest
from test_generator import load_test  # Adjust the import path to your project structure.

def find_all_csvs_in_subdirectories(base_directory):
    """
    Recursively find all CSV files in the specified base directory and its subdirectories.
    """
    csv_files = []
    for root, _, files in os.walk(base_directory):
        for file in files:
            if file.endswith('.csv'):  # Look for CSV files
                csv_files.append(os.path.join(root, file))
    return csv_files

# Parametrize the test with all the CSV files found in the subdirectories
@pytest.mark.parametrize("csv_file", find_all_csvs_in_subdirectories("practice_tests"))
def test_load_test_nested_csvs(csv_file):
    """
    Test that load_test correctly processes all CSV files in nested subdirectories.
    """
    result = load_test(csv_file)

    assert len(result) > 0, f"The CSV file {csv_file} should not be empty."

    for row in result:
        assert isinstance(row, list), f"Row {row} is not a list."

    for row in result:
        assert len(result[row]) == 7, f"Row {row} does not have 7 columns"

