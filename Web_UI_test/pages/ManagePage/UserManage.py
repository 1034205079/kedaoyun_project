from my_pytest.kedaoyun_project.Web_UI_test.pages.BasePage import BasePage


# 等待admin可见，且切换frame
class UserPage(BasePage):
    admin_locator = "id", "topbar-user"
    user_manage = "link text", "用户管理"
    frame_locator = "tag name", "iframe"

    def assert_admin_visibility(self, timeout=5):
        """admin可见"""
        self.element_should_be_visibility(self.admin_locator, timeout)

    def admin_click(self):
        self.click(locator=self.admin_locator)

    def user_manage_click(self):
        self.click(locator=self.user_manage)

    def switch(self):
        self.change_frame(self.frame_locator)
