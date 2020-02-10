import os
import sys
import time
import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from project.Pages.viewTransactionPage import ViewTransactionPage
from project.Pages.fundWalletPage import FundWalletPage
from project.Pages.airtimeRechargePage import AirtimeRechargePage
from project.Pages.loginPage import LoginPage

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class AllTestCases(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        caps = dict()
        caps["platformName"] = "ANDROID"
        caps["platformVersion"] = "6.0.1"
        caps["noReset"] = False
        caps["deviceName"] = "Samsung S8"
        caps['autoGrantPermissions'] = True
        caps["appActivity"] = "com.lenddo.mobile.paylater.home.activity.SplashScreenActivity"
        caps["appPackage"] = "com.lenddo.mobile.paylater.staging"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def test_01_login(self):
        driver = self.driver
        login = LoginPage(driver)

        login.click_initial_buttons()
        time.sleep(0)
        login.enter_phone_number("08990001099")
        login.enter_pin("1234")
        login.click_sign_in()
        time.sleep(2)
        print("Login successfully")

    def test_02_airtime_recharge(self):
        driver = self.driver
        recharge = AirtimeRechargePage(driver)

        recharge.click_buy_airtime_button()
        time.sleep(9)
        recharge.enter_phone_number("08100067519")
        time.sleep(4)
        recharge.enter_airtime_price("1000")
        time.sleep(9)
        recharge.wallet_payment()

        time.sleep(6)
        TouchAction(driver).tap(x=275, y=1382).perform()
        TouchAction(driver).tap(x=534, y=1397).perform()
        TouchAction(driver).tap(x=825, y=1394).perform()
        TouchAction(driver).tap(x=286, y=1529).perform()
        time.sleep(7)
        recharge.success_payment()
        time.sleep(5)
        print("Recharged successfully")

    def test_03__fund_wallet(self):
        driver = self.driver
        fund = FundWalletPage(driver)

        time.sleep(5)
        fund.click_fund_wallet_button()
        time.sleep(5)
        fund.enter_amount_to_fund("1000")
        time.sleep(5)
        fund.proceed_to_fund()
        time.sleep(5)
        TouchAction(driver).tap(x=275, y=1382).perform()
        TouchAction(driver).tap(x=534, y=1397).perform()
        TouchAction(driver).tap(x=825, y=1394).perform()
        TouchAction(driver).tap(x=286, y=1529).perform()
        time.sleep(9)
        fund.navigate_back_home()
        print("Funded successfully")

    def test_04_view_transaction(self):
        driver = self.driver
        view = ViewTransactionPage(driver)

        view.click_transaction_button()
        time.sleep(8)
        view.select_correct_dates_from()
        time.sleep(4)
        view.select_correct_date_to()
        time.sleep(2)
        view.screenshot_and_save()
        time.sleep(3)
        print("screen-shot saved")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
