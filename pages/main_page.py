from pages.base_page import BasePage
from utils.locators import *

class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = calculatorPageLocations
        super().__init__(driver)  # Python3 version

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.CLEAR) else False

    def enter_expression(self, expression):
        valid_input = set('0123456789+-/*')
        parsed_expression = str(expression).replace(" ", "")
        for c in parsed_expression:
            if c in valid_input:
                if c == '1':
                    self.find_element(*self.locator.ONE).click()
                elif c == "2":
                    self.find_element(*self.locator.TWO).click()
                elif c ==  "3":
                    self.find_element(*self.locator.THREE).click()
                elif c ==  "4":
                    self.find_element(*self.locator.FOUR).click()
                elif c ==  "5":
                    self.find_element(*self.locator.FIVE).click()
                elif c ==  "6":
                    self.find_element(*self.locator.SIX).click()
                elif c ==  "7":
                    self.find_element(*self.locator.SEVEN).click()
                elif c ==  "8":
                    self.find_element(*self.locator.EIGHT).click()
                elif c ==  "9":
                    self.find_element(*self.locator.NINE).click()
                elif c ==  "0":
                    self.find_element(*self.locator.ZERO).click()
                elif c ==  "+":
                    self.find_element(*self.locator.ADDITION).click()
                elif c ==  "-":
                    self.find_element(*self.locator.SUBTRACT).click()
                elif c ==  "*":
                    self.find_element(*self.locator.MULTIPLY).click()
                elif c ==  "/":
                    self.find_element(*self.locator.DIVIDE).click()
                elif c ==  _:
                    print("Invalid input")
                    return
        self.find_element(*self.locator.EQUALS).click()
        
        return self.find_element(*self.locator.DISPLAY).text

    
    def check_numbers(self):
        self.find_element(*self.locator.CLEAR).click()
        self.find_element(*self.locator.ONE).click()
        if self.find_element(*self.locator.DISPLAY).text != "1":
            print("Failed at 1")
            return False
        self.find_element(*self.locator.CLEAR).click()
        self.find_element(*self.locator.TWO).click()
        if self.find_element(*self.locator.DISPLAY).text != "2":
            print("Failed at 2")
            return False
        self.find_element(*self.locator.CLEAR).click()
        self.find_element(*self.locator.THREE).click()
        if self.find_element(*self.locator.DISPLAY).text != "3":
            print("Failed at 3")
            return False
        self.find_element(*self.locator.CLEAR).click()
        self.find_element(*self.locator.FOUR).click()
        if self.find_element(*self.locator.DISPLAY).text != "4":
            print("Failed at 4")
            return False
        self.find_element(*self.locator.CLEAR).click()
        self.find_element(*self.locator.FIVE).click()
        if self.find_element(*self.locator.DISPLAY).text != "5":
            print("Failed at 5")
            return False
        self.find_element(*self.locator.CLEAR).click()
        self.find_element(*self.locator.SIX).click()
        if self.find_element(*self.locator.DISPLAY).text != "6":
            print("Failed at 6")
            return False
        self.find_element(*self.locator.CLEAR).click()
        self.find_element(*self.locator.SEVEN).click()
        if self.find_element(*self.locator.DISPLAY).text != "7":
            print("Failed at 7")
            return False
        self.find_element(*self.locator.CLEAR).click()
        self.find_element(*self.locator.EIGHT).click()
        if self.find_element(*self.locator.DISPLAY).text != "8":
            print("Failed at 8")
            return False
        self.find_element(*self.locator.CLEAR).click()
        self.find_element(*self.locator.NINE).click()
        if self.find_element(*self.locator.DISPLAY).text != "9":
            print("Failed at 9")
            return False
        self.find_element(*self.locator.CLEAR).click()
        self.find_element(*self.locator.ZERO).click()
        if self.find_element(*self.locator.DISPLAY).text != "0":
            print("Failed at 0")
            return False
        
        return True