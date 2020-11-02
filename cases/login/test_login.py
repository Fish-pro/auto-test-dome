from lib.webui import login_and_check


class TestLoginError:
    def test_UI_0001(self):
        print("\n用例UI-0001")
        alert_text = login_and_check(password="88888888")
        assert alert_text == "请输入用户名"

    def test_UI_0002(self):
        print("\n用例UI-0002")
        alert_text = login_and_check(username="byhy")
        assert alert_text == "请输入密码"

    def test_UI_0003(self):
        print("\n用例UI-0003")
        alert_text = login_and_check(username="byh", password="88888888")
        assert alert_text == "登录失败 : 用户名或者密码错误"

    def test_UI_0004(self):
        print("\n用例UI-0004")
        alert_text = login_and_check(username="byhy", password="8888888")
        assert alert_text == "登录失败 : 用户名或者密码错误"

    def test_UI_0005(self):
        print("\n用例UI-0005")
        alert_text = login_and_check(username="byh", password="888888888")
        assert alert_text == "登录失败 : 用户名或者密码错误"
