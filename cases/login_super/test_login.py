import pytest

from lib.webui import login_and_check


class TestLoginError:
    @pytest.mark.parametrize(
        "username, password, expectedalert",
        [
            (None, "88888888", "请输入用户名"),
            ("byhy", None, "请输入密码"),
            ("byh", "88888888", "登录失败 : 用户名或者密码错误"),
            ("byhy", "8888888", "登录失败 : 用户名或者密码错误"),
            ("byhy", "888888888", "登录失败 : 用户名或者密码错误"),
        ],
    )
    def test_UI_0001_0005(self, username, password, expectedalert):
        alert_text = login_and_check(username, password)
        assert alert_text == expectedalert
