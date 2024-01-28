from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
      def __init__(self, driver:WebDriver) -> None:
            self.driver = driver
            self.wait = WebDriverWait(driver, 20)
            
      def click_element(self, locator_type, locator_value):
            self.driver.find_element(locator_type, locator_value).click()
            
      def enter_text(self, locator_type, locator_value, text):
            # self.driver.find_element(locator_type, locator_value).clear()
            self.driver.find_element(locator_type, locator_value).send_keys(text)
                                                
      def remove_something(self, class_name):
            self.driver.execute_script(f"document.querySelector('.{class_name}').remove();")
            
      def enter(self):
            action = ActionChains(self.driver)
            action.send_keys(Keys.ENTER)
            action.perform()
      
      def wait_clickable(self,element):
            self.wait.until(EC.element_to_be_clickable(element))
            
      def wait_click(self, *elements):
            for element in elements:
                  self.wait.until(EC.element_to_be_clickable(element))
                  self.click_elements(element)
            
      def element_text(self, locator_type, locator_value):
            return self.driver.find_element(locator_type, locator_value).text
      
      def click_elements(self, *elements):
            for element in elements:
                  locator_type, locator_value = element
                  self.driver.find_element(locator_type, locator_value).click()
                  
      def click_text_in_elements(self, locator_type, locator_value, l1, l2):
            elements = self.driver.find_element(locator_type, locator_value)
            elements_childs = elements.find_elements(l1, l2)
            print(len(elements_childs))
            
      def parent_element(self, element):
            locator_type, locator_value = element
            return self.driver.find_element(locator_type, locator_value)
      
      def elements_in_parent(self, parent_element, element):
            locator_type, locator_value = element
            return parent_element.find_elements(locator_type, locator_value)
      
      def text_in_element(self, parent_element, element):
            locator_type, locator_value = element
            return parent_element.find_element(locator_type, locator_value).text
      
      def wait_dissapear(self, element):
            self.wait.until(EC.invisibility_of_element_located((element)))
    
      def exists(self, element):
            self.wait.until(EC.presence_of_element_located((element)))
            
      def href_in_element(self, parent_element, element):
            locator_type, locator_value = element
            a = parent_element.find_element(locator_type, locator_value)
            href = a.get_attribute('href')
            return href
      
      def screenshot(self):
            self.driver.save_screenshot('C:/Users/Michael/Desktop/A/screenshot.png')
            
      def get_url(self):
            return self.driver.current_url