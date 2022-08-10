#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 01 07:35:33 2022
@author: rivera

This tester file allows to validate the correctness of the produced output.csv files
"""
import sys
from csv_diff import load_csv, compare


def print_message(message):
    """Gets the data from a .yaml file.

    Parameters
    ----------
    message : str, required
        The message to display.
    """
    print('[' + sys.argv[0] + ']:', message)


def main():
    """The main entry point for the program.

    It requires the input file to be named as output.csv and a file that contains the expected output for the test
    (e.g., test01.csv) as an argument for the program
    """
    # Validate arguments
    if not len(sys.argv) == 2:
        print_message('Usage: ' + sys.argv[0] + ' <expected-output-csv>')
    else:
        # Get the arguments for the app
        given_output_file_path = 'output.csv'
        expected_output_file_path = sys.argv[1]
        try:
            # Obtain the yaml data
            given_file_data = load_csv(open(given_output_file_path))
            expected_data = load_csv(open(expected_output_file_path))
            # Obtain the differences
            result = compare(given_file_data, expected_data)
            if len(result['added']) > 0 or len(result['removed']) > 0 or len(result['changed']) > 0 or len(result['columns_added']) > 0 or len(result['columns_removed']) > 0:
                print_message('TEST FAILED.' + ' Differences are shown below:')
                print(result)
            else:
                print_message('TEST PASSED')
        except FileNotFoundError as fnf:
            print(print_message('ERROR: ' + fnf.strerror))


if __name__ == '__main__':
    main()
