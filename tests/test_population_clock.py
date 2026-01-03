import time
import pytest
from pages.population_page import PopulationPage

def test_world_population_clock(setup):
    page = PopulationPage(setup)
    page.open_page()
    print("\nLive world population count (press CTRL+C to stop):\n")
    try:
        while True:
            population = page.get_population_count()
            print(f"world Population: {population}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExecution stopped by user (CTRL+C).")