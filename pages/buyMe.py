from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from base.base_page import BasePage
from base.locators import BuyMeLocators as l


class BuyMe(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        BasePage.__init__(self, driver)
        
    def sign_up(self, name, email, password, validation):
        try:
            self.click_elements(l.SIGN_BUTTON, l.TOSIGN_BUTTON) # GOES  TO THE SIGNING PAGE, AND THEN TO SIGNING UP PAGE
        except ElementClickInterceptedException:
            self.click_element(*l.TOSIGN_BUTTON)
        self.enter_text(*l.NAME_INPUT, name)
        self.enter_text(*l.MAIL_INPUT, email)
        self.enter_text(*l.PASSWORD_INPUT, password)
        self.enter_text(*l.VALIDATE_INPUT, validation)
        self.click_element(*l.CONFIRM_BOX)
        self.click_element(*l.SUBMIT_BUTTON)
    
    def check_password_error(self):
        try:
            self.click_element(*l.VALIDATION_ERROR)
        except NoSuchElementException:
            assert False
        
    def check_email_error(self):
        try:
            self.click_element(*l.EMAIL_ERROR)
        except NoSuchElementException:
            assert False
            
    def log_in(self, email, password):
        try:
            self.click_elements(l.SIGN_BUTTON) # GOES  TO THE SIGNING PAGE, AND THEN TO SIGNING UP PAGE
        except ElementClickInterceptedException:
            pass
        self.enter_text(*l.LOG_EMAIL_INPUT, email)
        self.enter_text(*l.LOG_PASSWORD_INPUT, password)
        self.click_element(*l.LOG_BUTTON)
        
    def is_entered(self):
        self.click_element(*l.ACOUNT_BUTTON)
    
    def check_log_password_error(self):
        self.click_element(*l.LOG_PASSWORD_ERROR)
        
    def check_log_email_error(self):
        self.click_element(*l.LOG_EMAIL_ERROR)
        
    def select_gift(self, amount, region, category):
        self.click_element(*l.AMOUNT_LIST)
        self.click_element(*l.find_option(amount))
        self.click_element(*l.REGION_LIST)
        self.click_element(*l.find_option(region))
        self.click_element(*l.CATEGORY_LIST)
        self.click_element(*l.find_option(category))
        self.click_element(*l.SEARCH_BUTTON)
    
    def sort_results(self, count):
        elements = self.elements_in_parent(self.parent_element(l.RESULTS_GRID), l.RESULT_CARD)
        row = 1
        if(count > len(elements)):
            print('Not enough results to print')
            count = len(elements)
        with open('gift_data.txt', 'w', encoding='utf-8') as file:
            for element in elements[:count]:
                title = self.text_in_element(element, l.CARD_NAME)
                file.write(f"{row}. The gift's title is: {title} \n")
                
    def pick_gift(self, number):
        number = number - 1
        elements = self.elements_in_parent(self.parent_element(l.RESULTS_GRID), l.RESULT_CARD)
        if(number > len(elements)):
            print("The number's too high to pick that gift")
            number = 0
        elements[number].click()
    
    def gift_type(self):
        elements = self.elements_in_parent(self.parent_element(l.GIFT_GRID), l.GIFT_CARD)
        elements[1].click()
        
    def enter_details(self, name, message):
        self.enter_text(*l.RECIEVER_NAME, name)
        self.enter_text(*l.RECIEVER_MESSAGE, message)
        self.click_element(*l.SEND_BUTTON)
    
    def send_email(self, email, name):
        elements = self.elements_in_parent(self.parent_element(l.SENDING_GRID), l.SEND_OPTION)
        elements[1].click()
        self.enter_text(*l.RECIEVER_MAIL, email)
        self.enter_text(*l.SENDER_NAME, name)
        
    def send_sms(self, number, sender_number, name):
        elements = self.elements_in_parent(self.parent_element(l.SENDING_GRID), l.SEND_OPTION)
        elements[0].click()
        self.enter_text(*l.RECIEVER_PHONE, number)
        self.enter_text(*l.SENDER_PHONE, sender_number)
        self.enter_text(*l.SENDER_NAME, name)
    
    def print_gift(self, name):
        elements = self.elements_in_parent(self.parent_element(l.SENDING_GRID), l.SEND_OPTION)
        elements[2].click()
        self.enter_text(*l.SENDER_NAME, name)