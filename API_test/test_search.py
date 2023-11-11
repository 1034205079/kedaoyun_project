import requests, time, pytest, allure


@allure.epic("可道云接口测试")
@allure.feature("用户管理")
class TestSc:

    @allure.severity("critical")
    @allure.title("正确的参数成功找到全部用户")
    def test_search(self, admin_token):
        url = "http://localhost:8989/?systemMember/get"
        r = requests.get(url, params={"accessToken": admin_token})
        print(r.json())
        assert r.json().get("code") == True


if __name__ == '__main__':
    pytest.main(["-vs", __file__])
