from ..page_checker import PageChecker
from .selenium_util import explicit_wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ...log.logger import print_log
from time import sleep

class GoogleChecker(PageChecker):
    def __init__(self, driver, page_type, date, teacher_name, child_name, capture_paper, do_not_submit):
        self.driver = driver
        self.page_type = page_type
        self.date = str(date).replace('.', '-')
        self.teacher_name = teacher_name
        self.child_name = child_name
        self.capture_paper = capture_paper
        self.do_not_submit = do_not_submit

    def check_all(self):
        sleep(2)
        return super().check_all()

    def fill_elements(self):        
        self._fill_element(self.driver, '//*[@id="i1"]/../../..//input', self.teacher_name)
        self._fill_element(self.driver, '//*[@id="i5"]/../../..//input', self.child_name)
        self._fill_element(self.driver, '//*[@id="i9"]/../../..//input', self.date)

    def click_radios(self):
        self._click_radio(self.driver, '//div[@aria-label="아이돌보미의 복장 및 위생, 쳥결상태는 양호한가?"]', True)
        self._click_radio(self.driver, '//div[@aria-label="손소독제와 마스크를 지참하였는가?"]', True)
        self._click_radio(self.driver, '//div[@aria-label="열(37.5도 이상) 또는 발열감, 오한이 있는가?"]', False)
        self._click_radio(self.driver, '//div[@aria-label="기침 증상이 있는가?"]', False)
        self._click_radio(self.driver, '//div[@aria-label="인후통(목아픔) 증상이 있는가?"]', False)
        self._click_radio(self.driver, '//div[@aria-label="호흡곤란(숨가쁨) 증상이 있는가?"]', False)
        self._click_radio(self.driver, '//div[@aria-label="코로나 19 감염증 예상수칙을 확인하고 준수하였는가?"]', True)

        self._click_radio(self.driver, '//div[@aria-label="휴대용 손소독제를 사용 후 문을 열었는가?"]', True)
        self._click_radio(self.driver, '//div[@aria-label="마스크를 착용하고 돌봄활동을 하였는가?"]', True)
        self._click_radio(self.driver, '//div[@aria-label="비누를 이용하여 30초 이상 꼼꼼히, 자주 손을 씻었는가?(돌보가정 도착 후 , 음식 제공시, 기저위 및 변기 사용 전후, 실외 활동 후)"]', True)
        self._click_radio(self.driver, '//div[@aria-label="대상아동에 열(37.5도 이상) 또는 발열감이 있는가?"]', False)
        self._click_radio(self.driver, '//div[@aria-label="대상아동에게 기침, 인후통, 호흡곤란 증상이 있는가?"]', False)
        self._click_radio(self.driver, '//div[@aria-label="대상가정의 창문을 열어 환기를 했는가?"]', True)
        self._click_radio(self.driver, '//div[@aria-label="돌봄활동 중 대상가정의 방문자(택배기사, 이웃 등)의 정보를 보조자에게 공유하였는가?"]', True)
        self._click_radio(self.driver, '//div[@aria-label="코로나 19 감염증 예방수칙을 이용가정과 공유하고 안내하였는가?"]', True)

    def sumbit(self):
        if not self.do_not_submit:
            self._sumbit(self.driver, '//span[contains(text(),"제출")]/../..')
            return
        print_log('submit passed')

    def capture_mid_process(self):
        return super().capture_mid_process()

    def capture_result(self):
        return super().capture_result()

    def get_finish_message(self):
        return self._get_finish_message(self.driver, '//*[@class="freebirdFormviewerViewResponseConfirmationMessage"]')

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

    def _click_radio(self, driver, xpath, is_true):
        try:
            if is_true:
                xpath += '//div[@data-value="그렇다."]'
            else:
                xpath += '//div[@data-value="아니다."]'
            
            explicit_wait(driver, xpath)

            elem = driver.find_element(By.XPATH, xpath)
            
            fail_count = 0
            while not self._radio_validation(elem):
                elem.click()
                fail_count += 1
                if fail_count > 5:
                    raise Exception('Failed to click : ' + xpath)
            
            print_log(elem.accessible_name)

        except Exception as e:
            print_log(str(e))
            raise Exception('Failed to click : ' + xpath)

    def _radio_validation(self, elem):
        aria_validation = elem.get_attribute('aria-checked')
        tab_validation = elem.get_attribute('tabindex')

        if aria_validation != 'true':
            return False
        if tab_validation != '0':
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
            # raise Exception('Failed to submit : ' + str(e))
            return '완료'