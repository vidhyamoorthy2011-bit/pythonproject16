import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup():
    options = Options()
    options.add_argument("--headless=new")       # run headless
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")         # useful for CI/Jenkins
    options.add_argument("--disable-dev-shm-usage")  # useful for CI


    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(10)
    yield driver
    driver.quit()
