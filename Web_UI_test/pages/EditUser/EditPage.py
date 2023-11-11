from my_pytest.kedaoyun_project.Web_UI_test.pages.BasePage import BasePage


class EditPage(BasePage):
    name = "xpath", "//input[@name='name']"
    nickname = "xpath", "//input[@name='nickName']"
    password = "xpath", "//input[@name='password']"
    roles = "xpath", '//button[@class="btn btn-default btn-xs"]'
    admin = "link text", 'Administrator'
    save = "xpath", "//button[@id='system-save']"

    def select_user(self, user: str):
        self.click(("link text", user))  # 自定义要修改的用户

    def edit_info(self, name, nickname, password):
        self.input_text(self.name, name)
        self.input_text(self.nickname, nickname)
        self.input_text(self.password, password)

    def select_admin(self):
        self.click(self.roles)
        self.click(self.admin)

    def confirm(self):
        self.click(self.save)

    def asser_disappear(self):
        self.element_should_be_disappear(self.save)
