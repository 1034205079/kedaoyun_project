import time

from my_pytest.kedaoyun_project.Web_UI_test.pages.home_Login.loginpage import LoginPage
from my_pytest.kedaoyun_project.Web_UI_test.pages.ManagePage.UserManage import UserPage
from PIL import ImageGrab
import allure


# 调用登陆页面，传入账户密码验证码，
@allure.epic("可道云web测试")
@allure.feature("用户管理")
@allure.story("登录")
class TestLogin(object):

    @allure.title("输入正确的信息成功登录")
    @allure.severity("blocker")
    def test_login(self, browser):
        """调取页面中的功能"""
        lp = LoginPage(browser)  # 实例化的时候需要浏览器driver。
        lp.input_username("admin")
        lp.input_password("123456")
        lp.click_login_button()
        sp = UserPage(browser)
        sp.assert_admin_visibility()  # 断言admin可见

    def teardown_method(self):
        loging_result = r"D:\PycharmProjects\pythonProject\my_pytest\kedaoyun_project\Web_UI_test\screenshots\登录测试结果.png"
        time.sleep(1)
        ImageGrab.grab().save(loging_result)
        allure.attach.file(loging_result, "截图", allure.attachment_type.PNG)
