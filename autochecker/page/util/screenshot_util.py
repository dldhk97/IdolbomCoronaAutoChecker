import os
from Screenshot import Screenshot_Clipping

def clip_current_screen(driver):
    path = os.path.join(_get_image_directory(), 'result.png')
    return driver.save_screenshot(path)

def clip_full_screen(driver):
    try:
        path = _get_image_directory()
        ob = Screenshot_Clipping.Screenshot()
        ob.full_Screenshot(driver, save_path=path, image_name='paper_image.png')
    except Exception as e:
        pass

def _get_image_directory():
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    root_path = os.path.abspath(os.path.join(os.path.join(os.path.join(absolute_path, os.pardir), os.pardir), os.pardir))
    return os.path.join(root_path, os.path.join('static', 'image'))