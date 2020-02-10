import time
from project.Locators.locators import Locators


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.carbon_up_button_id = Locators.carbon_up_button_id
        self.skip_tutorials_button_id = Locators.skip_tutorials_button_id
        self.sign_in_button1_id = Locators.sign_in_button1_id
        self.phone_number_textbox1_id = Locators.phone_number_textbox1_id
        self.enter_pin_textbox_id = Locators.enter_pin_textbox_id
        self.sign_in_button2_id = Locators.sign_in_button2_id
        self.not_right_now_button_id = Locators.not_right_now_button_id

    def click_initial_buttons(self):
        self.driver.find_element_by_id(Locators.carbon_up_button_id)\
            .click()
        time.sleep(8)
        self.driver.find_element_by_id(Locators.skip_tutorials_button_id)\
            .click()
        time.sleep(8)
        self.driver.find_element_by_id(Locators.sign_in_button1_id).click()
        time.sleep(8)

    def enter_phone_number(self, phonenumber):
        self.driver.find_element_by_id(Locators.phone_number_textbox1_id).send_keys(phonenumber)

    def enter_pin(self, pin):
        self.driver.find_element_by_id(Locators.enter_pin_textbox_id)\
            .send_keys(pin)
        time.sleep(2)

    def click_sign_in(self):
        self.driver.find_element_by_id(Locators.sign_in_button2_id).click()
        time.sleep(9)
        self.driver.find_element_by_id(Locators.not_right_now_button_id).click()
        time.sleep(5)
