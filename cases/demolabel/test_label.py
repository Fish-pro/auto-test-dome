import pytest

pytestmark = [pytest.mark.haha, pytest.mark.hehe]


@pytest.mark.hello
class TestLabel:
    @pytest.mark.webtest
    def test_c001021(self):
        print("\n用例C001021")
        assert 1 == 1
