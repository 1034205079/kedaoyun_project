from my_pytest.kedaoyun_project.Web_UI_test.pages.BasePage import BasePage


class DelUser(BasePage):
    del_button = "link text", "删除"
    confirm_button = "xpath", "//button[text()='确定']"

    def del_user(self,user):
        self.click(("link text", user))  # 自定义要删除的用户

    def click_del(self):
        self.click(self.del_button)

    def confirm_del(self):
        self.click(self.confirm_button)

    def assert_user_disppear(self):
        self.element_should_be_disappear(self.confirm_button)
