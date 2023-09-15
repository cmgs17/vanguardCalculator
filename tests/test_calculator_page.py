import unittest
from tests.base_test import BaseTest
from pages.main_page import *
from utils.test_cases import test_cases


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestCalculatorPage(BaseTest):

    def test_page_load(self):
        print("\n" + str(test_cases(0)))
        page = MainPage(self.driver)
        self.assertTrue(page.check_page_loaded())

    def test_addition(self):
        print("\n" + str(test_cases(1)))
        page = MainPage(self.driver)
        addition_result = page.enter_expression('5+2')
        self.assertIn("7", addition_result)

    def test_subtraction(self):
        print("\n" + str(test_cases(2)))
        page = MainPage(self.driver)
        subtraction_result = page.enter_expression('5-2')
        self.assertIn("3", subtraction_result)

    def test_multiplication(self):
        print("\n" + str(test_cases(3)))
        page = MainPage(self.driver)
        multiplication_result = page.enter_expression('5*2')
        self.assertIn("10", multiplication_result)

    def test_division(self):
        print("\n" + str(test_cases(4)))
        page = MainPage(self.driver)
        division_result = page.enter_expression('10/2')
        self.assertIn("5", division_result)

    def test_custom_expression(self):
        print("\n" + str(test_cases(5)))
        page = MainPage(self.driver)
        custom_result = page.enter_expression('10-8*3')
        self.assertIn("6", custom_result)

    def test_numbers(self):
        print("\n" + str(test_cases(6)))
        page = MainPage(self.driver)
        self.assertTrue(page.check_numbers())
