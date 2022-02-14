from ..page_checker import PageChecker

class GoogleChecker(PageChecker):
    def __init__(self, driver, page_type, date, teacher_name, child_name, capture_paper, do_not_submit):
        self.driver = driver
        self.page_type = page_type
        self.date = date
        self.teacher_name = teacher_name
        self.child_name = child_name
        self.capture_paper = capture_paper
        self.do_not_submit = do_not_submit

    def check_all(self):
        return super().check_all()

    def fill_elements(self):
        return super().fill_elements()

    def click_radios(self):
        return super().click_radios()

    def sumbit(self):
        return super().sumbit()

    def capture_mid_process(self):
        return super().capture_mid_process()

    def capture_result(self):
        return super().capture_result()

    def get_finish_message(self):
        return super().get_finish_message()