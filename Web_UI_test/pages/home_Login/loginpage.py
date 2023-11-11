from my_pytest.kedaoyun_project.Web_UI_test.pages.BasePage import BasePage


# 调用BasePage的动作方法来完成登录操作，本页面主要用输入和点击功能，并未输入账户密码的值
class LoginPage(BasePage):
    username_locator = "id", "username"  # 用户输入框定位器
    password_locator = "id", "password"  # 密码输入框定位器
    login_button_locator = "id", 'submit'  # 登录按钮定位器

    def input_username(self, username):
        """输入用户名功能"""
        self.input_text(locator=self.username_locator, text=username, clear=True)

    def input_password(self, password):
        """输入密码功能"""
        self.input_text(locator=self.password_locator, text=password, clear=True)

    def click_login_button(self):
        """点击登录按钮"""
        self.click(locator=self.login_button_locator)
