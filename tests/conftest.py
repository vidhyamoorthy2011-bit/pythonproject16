import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


@pytest.fixturegit
def setup():
    options = Options()
    options.add_argument("--headless=True")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=options)

    yield driver
    driver.quit()
