from my_pytest.kedaoyun_project.Web_UI_test.pages.EditUser.EditPage import EditPage
import time, allure
from PIL import ImageGrab


@allure.epic("可道云web测试")
@allure.feature("用户管理")
@allure.story("编辑用户")
class TestEdit:

    @allure.title("输入正确的信息成功修改")
    @allure.severity("normal")
    def test_edit(self, switch_frame):
        nickname = "xiaofei" + str(time.time())[-4:]
        ep = EditPage(switch_frame)
        ep.select_user("xiaofei")
        ep.edit_info(name=nickname, nickname="xiaofei", password="123456")
        ep.select_admin()
        ep.confirm()
        time.sleep(1)
        ep.asser_disappear()  # 断言界面消失

    def teardown_method(self):
        loging_result = r"D:\PycharmProjects\pythonProject\my_pytest\kedaoyun_project\Web_UI_test\screenshots\编辑用户结果.png"
        ImageGrab.grab().save(loging_result)
        allure.attach.file(loging_result, "截图", allure.attachment_type.PNG)
