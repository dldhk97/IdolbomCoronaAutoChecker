from abc import *
from .util.screenshot_util import clip_full_screen, clip_current_screen
from time import sleep

class PageChecker(metaclass=ABCMeta):
    driver = None
    page_type = None
    date = None
    teacher_name = None
    child_name = None
    capture_paper = None

    def check_all(self):
        # fill text
        self.fill_elements()

        # click radio
        self.click_radios()

        # capture mid-process paper
        self.capture_mid_process()

        # submit
        self.sumbit()

        # capture result
        self.capture_result()

        return self.get_finish_message()

    
    def fill_elements(self):
        pass

    def click_radios(self):
        pass

    def sumbit(self):
        pass

    def capture_mid_process(self):
        if self.capture_paper:
            clip_full_screen(self.driver)

    def capture_result(self):
        sleep(1)
        clip_current_screen(self.driver)

    def get_finish_message(self):
        pass