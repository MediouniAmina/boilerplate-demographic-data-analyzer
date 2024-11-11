# main.py

# Import the demographic_data_analyzer module, which contains the calculate_demographic_data function
import demographic_data_analyzer
from unittest import main

# Test the function by calling it here
# It will print the demographic analysis results to the console
demographic_data_analyzer.calculate_demographic_data()

# Run unit tests automatically
# This will check if the function passes all tests defined in test_module.py
main(module='test_module', exit=False)
