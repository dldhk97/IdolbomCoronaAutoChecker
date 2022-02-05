import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ..log.logger import print_log
from .screenshot_util import clip_full_screen, clip_current_screen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def check_all(driver, date, teacher_name, child_name, capture_screenshot):
    _fill_elements(driver, date, teacher_name, child_name)

    # 자기 건강 체크
    _self_health_check(driver)

    # 이용가정 방문 체크
    _visit_check(driver)

    # 중간과정 스크린샷 캡쳐
    if capture_screenshot:
        clip_full_screen(driver)
    else:
        sleep(1)

    if not os.environ.get('DO_NOT_SUBMIT'):
        _sumbit(driver, '//*[@id="pageNav"]/*[@menu="submitBtn"]')
    else:
        print_log('Pass submit')
    
    clip_current_screen(driver)

def _fill_elements(driver, date, teacher_name, child_name):
    _fill_element(driver, '//*[@id="date_6"]', date)
    _fill_element(driver, '//*[@id="formItem_7"]/div/div[3]/div/input', teacher_name)
    _fill_element(driver, '//*[@id="formItem_8"]/div/div[3]/div/input', child_name)

def _self_health_check(driver):
    _click_radio(driver, 'gridRow_0_1', True)
    _click_radio(driver, 'gridRow_1_1', True)
    _click_radio(driver, 'gridRow_2_1', False)
    _click_radio(driver, 'gridRow_3_1', False)
    _click_radio(driver, 'gridRow_4_1', False)
    _click_radio(driver, 'gridRow_5_1', False)
    _click_radio(driver, 'gridRow_6_1', True)

def _visit_check(driver):
    _click_radio(driver, 'gridRow_0_4', True)
    _click_radio(driver, 'gridRow_1_4', True)
    _click_radio(driver, 'gridRow_2_4', True)
    _click_radio(driver, 'gridRow_3_4', False)
    _click_radio(driver, 'gridRow_4_4', False)
    _click_radio(driver, 'gridRow_5_4', True)
    _click_radio(driver, 'gridRow_6_4', True)
    _click_radio(driver, 'gridRow_7_4', True)

def _fill_element(driver, xpath, text):
    try:
        _explicit_wait(driver, xpath)
        elem = driver.find_element(By.XPATH, xpath)
        elem.send_keys(text)

        if not _fill_validation(elem, text):
            raise Exception('Validation failed')
        
        print_log(elem.accessible_name + ' : ' + text)
        
    except Exception as e:
        raise Exception('Failed to fill : ' + xpath)

def _fill_validation(elem, text):
    validation = elem.get_attribute('value')
    return validation == text
    
def _click_radio(driver, id, is_true):
    try:
        value = '아니다'
        if is_true:
            value = '그렇다'
        xpath = '//*[@id="' + id + '" and @value="' + value + '"]'
        
        _explicit_wait(driver, xpath)
        elem = driver.find_element(By.XPATH, xpath)

        driver.execute_script("arguments[0].setAttribute('checked','true')", elem)
        driver.execute_script("arguments[0].setAttribute('aria-checked','true')", elem)
        driver.execute_script("arguments[0].setAttribute('class','gridRadio gridRow_0_1 ui_radio ui_component check')", elem)

        if not _radio_validation(elem):
            raise Exception('Validation failed')
        
        print_log(elem.accessible_name)

    except Exception as e:
        raise Exception('Failed to click : ' + id)

def _radio_validation(elem):
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

def _sumbit(driver, xpath):
    try:
        elem = driver.find_element(By.XPATH, xpath)
        elem.send_keys(Keys.ENTER)
    except Exception as e:
        raise Exception('Failed to click : ' + xpath)

def _explicit_wait(driver, xpath):
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located\
	                ((By.XPATH, xpath)))
    except Exception as e:
        pass