import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


@pytest.fixture
def setup():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")

    options.binary_location = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

    service = Service()

    driver = webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(10)

    yield driver
    driver.quit()

