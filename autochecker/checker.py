import os
from .driver.loader import load_driver
from .page.page_checker_factory import create_page_checker
from .log.logger import print_log


def check(child_name, date, capture_paper):
    is_succeed = False
    result_msg = '제출 완료'
    try:
        _check_env()
        driver = load_driver(os.environ.get('CHROME_DRIVER_VERSION'))

        url = os.environ.get('SELF_CHECK_URL')
        _open_page(driver, url)
        print_log('Page open succeed!')

        page_checker = create_page_checker(driver, date, child_name, capture_paper, url)

        finish_msg = page_checker.check_all()
        is_succeed = True

    except Exception as e:
        print_log(e)
        result_msg = '오류 발생'
        finish_msg = str(e)
    try:
        driver.quit()
    except:
        pass

    return is_succeed, result_msg, finish_msg

def _check_env():
    if os.path.exists('./.env') == False:
        raise Exception('No .env file! Please create .env file!')

def _open_page(driver, url):
    driver.get(url=url)