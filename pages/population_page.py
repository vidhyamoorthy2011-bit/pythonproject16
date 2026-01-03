from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PopulationPage:
    URL = "https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live"
    POPULATION_COUNT = "//div[contains(@class,'counter-ticker')]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self):
        self.driver.get(self.URL)

    def get_population_count(self):
        population = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.POPULATION_COUNT)))
        return population.text