import os
import time
from project.Locators.locators import Locators


class ViewTransactionPage():
    def __init__(self, driver):
        self.driver = driver

        self.view_wallet_transaction_button_id = Locators.view_wallet_transaction_button_id
        self.title_menu_button_id = Locators.title_menu_button_id
        self.date_range_from_button_id = Locators.date_range_from_button_id
        self.date_range_to_button_id = Locators.date_range_to_button_id
        self.select_date_button_id = Locators.select_date_button_id

    def click_transaction_button(self):
        self.driver.find_element_by_id(Locators.view_wallet_transaction_button_id).click()

    def select_correct_dates_from(self):
        self.driver.find_element_by_id(Locators.title_menu_button_id).click()

        self.driver.find_element_by_id(Locators.date_range_from_button_id).click()
        self.driver.find_element_by_id(Locators.select_date_button_id).click()

    def select_correct_date_to(self):
        self.driver.find_element_by_id(Locators.date_range_to_button_id).click()
        self.driver.find_element_by_id(Locators.select_date_button_id).click()






