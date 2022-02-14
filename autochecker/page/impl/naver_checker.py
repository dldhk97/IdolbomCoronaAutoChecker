from ..page_checker import PageChecker
from ..util.selenium_util import explicit_wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ...log.logger import print_log

class NaverChecker(PageChecker):
    def __init__(self, driver, page_type, date, teacher_name, child_name, capture_paper, do_not_submit):
        self.driver = driver
        self.page_type = page_type
        self.date = date
        self.teacher_name = teacher_name
        self.child_name = child_name
        self.capture_paper = capture_paper
        self.do_not_submit = do_not_submit

    def check_all(self):
        return super().check_all()

    def fill_elements(self):
        self._fill_element(self.driver, '//*[@id="date_6"]', self.date)
        self._fill_element(self.driver, '//*[@id="formItem_7"]/div/div[3]/div/input', self.teacher_name)
        self._fill_element(self.driver, '//*[@id="formItem_8"]/div/div[3]/div/input', self.child_name)

    def click_radios(self):
        self._click_radio(self.driver, 'gridRow_0_1', True)
        self._click_radio(self.driver, 'gridRow_1_1', True)
        self._click_radio(self.driver, 'gridRow_2_1', False)
        self._click_radio(self.driver, 'gridRow_3_1', False)
        self._click_radio(self.driver, 'gridRow_4_1', False)
        self._click_radio(self.driver, 'gridRow_5_1', False)
        self._click_radio(self.driver, 'gridRow_6_1', True)

        self._click_radio(self.driver, 'gridRow_0_4', True)
        self._click_radio(self.driver, 'gridRow_1_4', True)
        self._click_radio(self.driver, 'gridRow_2_4', True)
        self._click_radio(self.driver, 'gridRow_3_4', False)
        self._click_radio(self.driver, 'gridRow_4_4', False)
        self._click_radio(self.driver, 'gridRow_5_4', True)
        self._click_radio(self.driver, 'gridRow_6_4', True)
        self._click_radio(self.driver, 'gridRow_7_4', True)

    def sumbit(self):
        if not self.do_not_submit:
            self._sumbit(self.driver, '//*[@id="pageNav"]/*[@menu="submitBtn"]')
        

    def capture_mid_process(self):
        return super().capture_mid_process()

    def capture_result(self):
        return super().capture_result()

    def get_finish_message(self):
        return self._get_finish_message(self.driver, '//*[@class="finishMessage"]')

    def _fill_element(self, driver, xpath, text):
        try:
            explicit_wait(driver, xpath)
            elem = driver.find_element(By.XPATH, xpath)
            elem.send_keys(text)

            if not self._fill_validation(elem, text):
                raise Exception('Validation failed')
            
            print_log(elem.accessible_name + ' : ' + text)
            
        except Exception as e:
            raise Exception('Failed to fill : ' + xpath)
        
    def _fill_validation(self, elem, text):
        validation = elem.get_attribute('value')
        return validation == text

    def _click_radio(self, driver, id, is_true):
        try:
            value = '아니다'
            if is_true:
                value = '그렇다'
            xpath = '//*[@id="' + id + '" and @value="' + value + '"]'
            
            explicit_wait(driver, xpath)
            elem = driver.find_element(By.XPATH, xpath)

            driver.execute_script("arguments[0].setAttribute('checked','true')", elem)
            driver.execute_script("arguments[0].setAttribute('aria-checked','true')", elem)
            driver.execute_script("arguments[0].setAttribute('class','gridRadio gridRow_0_1 ui_radio ui_component check')", elem)

            if not self._radio_validation(elem):
                raise Exception('Validation failed')
            
            print_log(elem.accessible_name)

        except Exception as e:
            raise Exception('Failed to click : ' + id)

    def _radio_validation(self, elem):
        checked = elem.get_attribute('checked')
        aria_checked = elem.get_attribute('aria-checked')
        class_validation = elem.get_attribute('class')

        if checked != 'true':
            return False
        if aria_checked != 'true':
            return False
        if class_validation != 'gridRadio gridRow_0_1 ui_radio ui_component check':
            return False
        return True

    def _sumbit(self, driver, xpath):
        try:
            elem = driver.find_element(By.XPATH, xpath)
            elem.send_keys(Keys.ENTER)
        except Exception as e:
            raise Exception('Failed to click : ' + xpath)

    def _get_finish_message(self, driver, xpath):
        try:
            explicit_wait(driver, xpath)
            elem = driver.find_element(By.XPATH, xpath)
            
            finish_message = elem.text
            print_log(finish_message)

            return finish_message

        except Exception as e:
            raise Exception('Failed to submit : ' + str(e))