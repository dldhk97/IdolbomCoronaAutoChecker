from lib2to3.pgen2 import driver
import requests
import os
import wget
import zipfile
from .platform_util import get_archive_file_name_by_platform, is_driver_excutable_file_exists
from ..log.logger import print_log

def download_driver(driver_version):
    print_log('chromedriver download start!')

    if not driver_version:
        driver_version = _get_latest_version()

    base_url = os.environ.get('CHROME_DRIVER_URL') + driver_version + '/'
    file_name = get_archive_file_name_by_platform()
    download_url = base_url + file_name

    print_log('chromedriver download started!')
    latest_driver_zip = wget.download(download_url, file_name)
    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        zip_ref.extractall()
    os.remove(latest_driver_zip)
    print_log('chromedriver download complete!')   

def _get_latest_version():
    url = os.environ.get('CHROME_DRIVER_URL') + 'LATEST_RELEASE'

    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        print_log(response.status_code)
        raise Exception('Failed to get latest chromedriver version')