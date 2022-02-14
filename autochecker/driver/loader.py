import os
from selenium import webdriver
from .downloader import download_driver 
from .platform_util import is_driver_excutable_file_exists, get_driver_excutable_file_path
from ..log.logger import print_log

def load_driver():
    download_driver()

    if not is_driver_excutable_file_exists():
        raise Exception('No chromedriver!')

    options = _get_options()
    
    driver_path = get_driver_excutable_file_path()
    print_log('chrome_driver_path=' + driver_path)

    try:
       os.chmod(driver_path, 0o0777)
    except Exception as e:
       print_log('Failed to chmod driver')
       print_log(e)

    return webdriver.Chrome(executable_path=driver_path, chrome_options=options)

def _get_options():
    options = webdriver.ChromeOptions()
    
    # Enable headless mode
    options.add_argument('headless')
    options.add_argument("no-sandbox")

    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR")
    options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    return options
