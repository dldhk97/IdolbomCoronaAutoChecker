import os
from selenium import webdriver
from .downloader import download_driver 
from .platform_util import is_driver_excutable_file_exists, get_driver_excutable_file_path
from ..log.logger import print_log

def load_driver(driver_version, retry=0):
    if not is_driver_excutable_file_exists() or retry > 0:
        download_driver(driver_version)

    options = _get_options()
    
    driver_path = get_driver_excutable_file_path()
    print_log('chrome_driver_path=' + driver_path)

    try:
       os.chmod(driver_path, 0o0777)
    except Exception as e:
       print_log('Failed to chmod driver')
       print_log(e)

    failed_exception = None
    try:
        return webdriver.Chrome(executable_path=driver_path, chrome_options=options)
    except Exception as e:
        failed_exception = e

    if not ('session not created: This version of ChromeDriver only supports Chrome version' in str(failed_exception)):
        raise failed_exception
    
    if retry == 0:
        return load_driver(driver_version, retry + 1)
    elif retry == 1:
        installed_driver_version = _find_installed_driver_version(str(failed_exception))
        print_log('installed driver version : ' + installed_driver_version)
        return load_driver(installed_driver_version, retry + 1)
    print_log('Failed to load driver : available driver not found')
    raise failed_exception

def _find_installed_driver_version(msg):
    start = msg.find('Current browser version is') + 27
    end = msg.find(' with binary path')
    return msg[start:end]

def _get_options():
    options = webdriver.ChromeOptions()
    
    # Enable headless mode
    if os.environ.get('HEADLESS_MODE') == 'True':
        options.add_argument('headless')
        options.add_argument("no-sandbox")

    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR")
    options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    return options
