from unittest import TestCase
from selenium import webdriver
from base.locators import Links as links
from pages.buyMe import BuyMe
import json
import time

class TestBuyMe(TestCase):
    def setUp(self) -> None:
        with open("data.json" , "r") as file:
            data = json.loads(file.read())
            
        if data["headless"]:
            if data["browser"] == "firefox":
                options = webdriver.FirefoxOptions()
                options.add_argument("--headless")
                self.driver = webdriver.Firefox(options=options)
            elif data["browser"] == "chrome":
                options = webdriver.ChromeOptions()
                options.add_argument("--headless")
                self.driver = webdriver.Chrome(options=options)
                
        elif data["browser"] == "firefox":
            self.driver = webdriver.Firefox()
            
        elif data["browser"] == "chrome":
            self.driver = webdriver.Chrome()
        
        self.driver.implicitly_wait(20)    
        self.driver.get(links.BUYME_LINK)
        self.buyme_page = BuyMe(self.driver)
        
    def test1_wrong_validation(self):
        self.buyme_page.sign_up("Michael", "goodemail@gmail.com", "12345678", "87654321")
        self.buyme_page.check_password_error()
        time.sleep(5)
        
    def test2_wrong_email(self):
        self.buyme_page.sign_up("Michael", "thisisnotanemail", "12345678", "12345678")
        self.buyme_page.check_email_error()
        time.sleep(5)
        
    def test3_sign_right(self):
        self.buyme_page.sign_up("Michael", "gefolap418@flexvio.com", "Aa12345678", "Aa12345678")
        self.buyme_page.is_entered() #Sometimes there is Recaptcha so it might fail
        time.sleep(5)
        
    def test4_log_wrong_passwrod(self):
        self.buyme_page.log_in("foxaj92846@taobudao.com", "1234")
        self.buyme_page.check_log_password_error()
        time.sleep(5)    
    
    def test5_log_wrong_email(self):
        self.buyme_page.log_in("gefolap418@flexvio.com", "Aa12345678")
        self.buyme_page.check_log_email_error()
        time.sleep(5)    
        
    def test6_buy_gift(self):
        self.buyme_page.log_in("xefaka4589@tsderp.com", "Aa12345678")
        self.buyme_page.select_gift("עד 99", "מרכז", "המתנות האהובות של 2024")
        self.buyme_page.pick_gift(400)
        self.buyme_page.gift_type()
        self.buyme_page.enter_details("ישראל ישראלי", "מזל טוב ליום הולדתך")
        self.buyme_page.send_sms("+972541231234", "+9721231234", "ישראל ישראלי")
        time.sleep(5)

    def tearDown(self) -> None:
        self.driver.quit()
        
            
        
            
                   