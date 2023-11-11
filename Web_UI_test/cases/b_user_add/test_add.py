from my_pytest.kedaoyun_project.Web_UI_test.pages.AddUser.AddUserPage import AddUser
from PIL import ImageGrab
import time, allure


@allure.epic("可道云web测试")
@allure.feature("用户管理")
@allure.story("添加用户")
class TestAdd:

    @allure.title("输入正确的信息成功添加")
    @allure.severity("critical")
    def test_add(self, switch_frame):
        name = "xiaofei" + str(time.time())[-4:]
        ad = AddUser(switch_frame)
        ad.create_new()
        ad.input_name(name)
        ad.input_nickname("xiaofei")
        ad.input_password("sxf199655")
        ad.choose_default_role()
        time.sleep(1)
        ad.submit()
        ad.assert_disapper()  # 断言添加按钮消失

    def teardown_method(self):
        loging_result = r"D:\PycharmProjects\pythonProject\my_pytest\kedaoyun_project\Web_UI_test\screenshots\添加用户结果.png"
        ImageGrab.grab().save(loging_result)
        allure.attach.file(loging_result, "截图", allure.attachment_type.PNG)
