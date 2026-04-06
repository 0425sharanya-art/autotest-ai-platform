from selenium import webdriver

def test_google():

    driver = webdriver.Chrome()

    driver.get("https://google.com")

    assert "Google" in driver.title

    driver.quit()
