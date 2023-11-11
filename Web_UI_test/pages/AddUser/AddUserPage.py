from my_pytest.kedaoyun_project.Web_UI_test.pages.BasePage import BasePage


class AddUser(BasePage):
    new_user = "xpath", "//button[text()='新建用户']"
    name_locator = "xpath", "//input[@name='name']"
    nickname_locator = "xpath", "//input[@name='nickName']"
    password_locator = "xpath", "//input[@name='password']"
    roles_locator = "xpath", "//button[@class='btn btn-default btn-xs']"  # 不是下拉框
    default_role = "link text", "default"  # 不是下拉框
    add_button = "id", "system-save"

    def create_new(self):
        self.click(self.new_user)

    def input_name(self, text: str):
        self.input_text(self.name_locator, text)

    def input_nickname(self, text: str):
        self.input_text(self.nickname_locator, text)

    def input_password(self, text: str):
        self.input_text(self.password_locator, text)

    def choose_default_role(self):
        self.click(self.roles_locator)
        self.click(self.default_role)

    def submit(self):
        self.click(self.add_button)

    def assert_disapper(self):
        self.element_should_be_disappear(self.add_button)