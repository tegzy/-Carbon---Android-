from project.Locators.locators import Locators
import time

class FundWalletPage():
    def __init__(self, driver):
        self.driver = driver

        self.fund_wallet_button_id = Locators.fund_wallet_button_id
        self.fund_wallet_card_id = Locators.fund_wallet_card_id
        self.fund_wallet_amount_id = Locators.fund_wallet_amount_id
        self.proceed_fund_wallet_id = Locators.proceed_fund_wallet_id
        self.image_check_button_id = Locators.image_check_button_id
        self.confirm_payment_button_id = Locators.confirm_payment_button_id
        self.secure_pay_button_id = Locators.secure_pay_button_id
        self.success_home_button_id = Locators.success_home_button_id
        self.okay_button_id = Locators.okay_button_id



    def click_fund_wallet_button(self):
        self.driver.find_element_by_id(Locators.fund_wallet_button_id)\
            .click()
        self.driver.find_element_by_id(Locators.fund_wallet_card_id)\
            .click()

    def enter_amount_to_fund(self, amount):
        self.driver.find_element_by_id(Locators.fund_wallet_amount_id)\
            .send_keys(amount)

    def proceed_to_fund(self):
        self.driver.find_element_by_id(Locators.proceed_fund_wallet_id).click()
        time.sleep(7)
        self.driver.find_element_by_id(Locators.image_check_button_id).click()
        time.sleep(7)
        self.driver.find_element_by_id(Locators.confirm_payment_button_id).click()
        time.sleep(7)
        self.driver.find_element_by_id(Locators.secure_pay_button_id).click()
        time.sleep(6)
    # pin entry

    def navigate_back_home(self):
        self.driver.find_element_by_id(Locators.success_home_button_id).click()
        time.sleep(5)
        self.driver.find_element_by_id(Locators.okay_button_id).click()

