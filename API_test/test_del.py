import requests, time, pytest, allure


@allure.epic("可道云接口测试")
@allure.feature("用户管理")
class TestDel:

    @allure.severity("normal")
    @allure.title("正确的id成功删除用户")
    def test_delete(self, admin_token):
        url = "http://localhost:8989/?systemMember/doAction"
        data = {"action": "del",  # 动作:删除用户;
                "userID": '["103"]'  # 用户id,用类似["23","344"]json方式包装}
                }

        r = requests.post(url, params={"accessToken": admin_token}, data=data)
        print(r.json())
        assert r.json().get("data") == "Successful operation"


if __name__ == '__main__':
    pytest.main(["-vs", __file__])
