import os
from urllib.parse import urlparse
from .enum.page_type import PageType
from .impl.naver_checker import NaverChecker
from .impl.google_checker import GoogleChecker

def _get_page_type(url):
    parse_result = urlparse(url)
    
    if 'naver' in parse_result.hostname:
        return PageType.NAVER
    if 'google' in parse_result.hostname:
        return PageType.GOOGLE

def create_page_checker(driver, date, child_name, capture_paper, url):
    page_type = _get_page_type(url)
    teacher_name = os.environ.get('TEACHER_NAME')
    do_not_submit = os.environ.get('DO_NOT_SUBMIT') == 'True'
    
    if page_type == PageType.NAVER:
        return NaverChecker(driver, page_type, date, teacher_name, child_name, capture_paper, do_not_submit)
    if page_type == PageType.GOOGLE:
        return GoogleChecker(driver, page_type, date, teacher_name, child_name, capture_paper, do_not_submit)