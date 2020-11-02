import time

from selenium import webdriver


def login_and_check(username=None, password=None):
    driver = webdriver.Chrome(r"/Users/york/projects/test/chromedriver")
    driver.implicitly_wait(10)
    driver.get("http://127.0.0.1/mgr/sign.html")
    if username:
        driver.find_element_by_id("username").send_keys(username)
    if password:
        driver.find_element_by_id("password").send_keys(password)

    driver.find_element_by_css_selector("button[type='submit']").click()

    time.sleep(1)

    alert_text = driver.switch_to.alert.text
    print(alert_text)
    driver.quit()
    return alert_text
