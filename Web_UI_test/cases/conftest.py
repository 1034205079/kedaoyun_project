import pytest, time, allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as firefox_service
from my_pytest.kedaoyun_project.Web_UI_test.pages.home_Login.loginpage import LoginPage
from my_pytest.kedaoyun_project.Web_UI_test.pages.ManagePage.UserManage import UserPage


@pytest.fixture(scope="class")
def browser():
    dr = webdriver.Firefox(service=firefox_service(log_output="firefox_log.log"))
    dr.maximize_window()
    dr.implicitly_wait(5)
    dr.get("http://localhost:8989/index.php?user/login")
    yield dr
    time.sleep(1)
    dr.quit()


@pytest.fixture(scope="class")
def admin_login(browser):
    lp = LoginPage(browser)  # 实例化的时候需要浏览器driver。
    lp.input_username("admin")
    lp.input_password("123456")
    lp.click_login_button()
    sp = UserPage(browser)
    sp.assert_admin_visibility()
    yield sp.dr


@pytest.fixture(scope="class")
def switch_frame(admin_login):
    up = UserPage(admin_login)
    up.admin_click()
    up.user_manage_click()
    up.switch()  # 切换frame
    yield up.dr
