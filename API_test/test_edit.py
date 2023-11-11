import requests, time, pytest, allure


@allure.epic("可道云接口测试")
@allure.feature("用户管理")
class TestEdit:

    @allure.severity("normal")
    @allure.title("正确的信息成功编辑用户")
    def test_edit(self, admin_token):
        url = "http://localhost:8989/?systemMember/edit"
        data = {"userID": 108,  # 用户id
                "name": "luoj1695174713",  # 可选；修改用户账号，无该字段则不修改
                "password": 654321,  # 可选；修改用户登陆密码，无该字段则不修改
                "sizeMax": 2,  # 可选；修改用户空间大小设置，无该字段则不修改
                "role": 2,  # 可选；修改用户角色id，无该字段则不修改
                "groupInfo": '{"1":"write"}'  # 可选；修改用户所在部门及在部门对应的权限，无该字段则不修改
                }
        r = requests.post(url, params={"accessToken": admin_token}, data=data)
        print(r.json())
        assert r.json().get("data") == "Successful operation"


if __name__ == '__main__':
    pytest.main(["-vs", __file__])
