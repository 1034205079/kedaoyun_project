import requests, base64, hashlib, pytest
from tools.De_Encrypt import De_en_tool


@pytest.fixture(scope="session")
def admin_token():
    login_token = base64.b64encode("admin".encode()).decode() + "|" + hashlib.md5(
        ("admin" + "1234567890").encode()).hexdigest()
    url = f"http://localhost:8989/?user/loginSubmit&isAjax=1&getToken=1&login_token={login_token}"  # 可以不用url编码直接送进来
    r = requests.get(url)
    return r.json().get("data")  # 拿到access token 然后直接用params={"accessToken": admin_token}来传


if __name__ == '__main__':
    admin_token()
