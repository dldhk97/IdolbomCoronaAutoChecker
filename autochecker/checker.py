import os
from .driver.loader import load_driver
from .page.check_page import check_all
from .log.logger import print_log

def check(child_name, date, capture_screenshot):
    msg = '정상적으로 처리되었습니다(대상 : ' + child_name + ', 날짜 : ' + date + ')'
    try:
        _check_env()
        driver = load_driver()

        url = os.environ.get('SELF_CHECK_URL')
        _open_page(driver, url)
        print_log('Page open succeed!')

        teacher_name = os.environ.get('TEACHER_NAME')

        check_all(driver, date, teacher_name, child_name, capture_screenshot)
        print_log('Done!')
    except Exception as e:
        print_log(e)
        msg = '오류 발생 : ' + str(e)
    try:
        driver.quit()
    except:
        pass

    return msg

def _check_env():
    if os.path.exists('./.env') == False:
        raise Exception('No .env file! Please create .env file!')

def _open_page(driver, url):
    driver.get(url=url)