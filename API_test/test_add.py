import requests, time, pytest, allure


@allure.epic("可道云接口测试")
@allure.feature("用户管理")
class TestUser:

    @allure.severity("blocker")
    @allure.title("正确的信息成功添加新用户")
    def test_add(self, admin_token):
        url = "http://localhost:8989/?systemMember/add"
        data = {"name": f"luoj{int(time.time())}",  # 用户账号
                "password": 123456,  # 用户密码
                "sizeMax": 2,  # 用户空间大小设置
                "role": 2,  # 用户角色id
                "groupInfo": '{"1":"write"}'}  # 用户所在部门及在部门对应的权限
        r = requests.post(url, params={"accessToken": admin_token}, data=data)
        assert r.json().get("data") == "Successful operation"


if __name__ == '__main__':
    pytest.main([__file__, "-vs"])
