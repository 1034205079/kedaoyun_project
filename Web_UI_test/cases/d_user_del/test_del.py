from my_pytest.kedaoyun_project.Web_UI_test.pages.DelPage.DelUserPage import DelUser
import allure
from PIL import ImageGrab


@allure.epic("可道云web测试")
@allure.feature("用户管理")
@allure.story("删除用户")
class Testdel:

    @allure.title("选择正确的用户成功删除")
    @allure.severity("normal")
    def test_del(self, switch_frame):
        dl = DelUser(switch_frame)
        dl.del_user("xiaofei")
        dl.click_del()
        dl.confirm_del()
        dl.assert_user_disppear()  # 断言

    def teardown_method(self):
        loging_result = r"D:\PycharmProjects\pythonProject\my_pytest\kedaoyun_project\Web_UI_test\screenshots\删除用户结果.png"
        ImageGrab.grab().save(loging_result)
        allure.attach.file(loging_result, "截图", allure.attachment_type.PNG)