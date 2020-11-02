import pytest


class TestLoginError3:
    @classmethod
    def setup_class(cls):
        print("\n === 初始化-类 ===")

    @classmethod
    def teardown_class(cls):
        print("\n === 清除 - 类 ===")

    def setup_method(self):
        print("\n --- 初始化-方法  ---")

    def teardown_method(self):
        print("\n --- 清除  -方法 ---")

    def test_c001001(self):
        print("\n用例C001001")
        assert 1 == 1

    def test_c001002(self):
        print("\n用例C001002")
        assert 2 == 2

    def test_c001003(self):
        print("\n用例C001003")
        assert 3 == 2


class TestLoginError4:
    @pytest.mark.hello
    @pytest.mark.webtest
    def test_c001021(self):
        print("\n用例C001021")
        assert 1 == 1

    def test_c001022(self):
        print("\n用例C001022")
        assert 2 == 2
