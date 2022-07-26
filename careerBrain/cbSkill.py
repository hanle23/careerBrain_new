import utils as UTIL
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import random


def fill_box(skill, driver):
    try:
        textBox = driver.find_element(By.XPATH, '//input[1]')
        textBox.clear()
        for char in skill:
            textBox.send_keys(char)
            textBox.send_keys(Keys.RETURN)
        buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "options"))).find_elements(By.TAG_NAME, 'option')
        for button in buttons:
            button.send_keys(Keys.RETURN)

    except TimeoutException:
        return skill
    except NoSuchElementException:
        print("No Such Element")


def process_skill(test_option, driver):
    skills = test_option[1].split(',')
    not_found = []
    for skill in skills:
        error = fill_box(skill.strip(), driver)
        if error == skill:
            not_found.append(error)
    try:
        WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "min-h-screen"))
        ).find_elements(By.LINK_TEXT, "Discover roles based on my skills")[
            0].click()
        WebDriverWait(driver, 100).until(
            EC.invisibility_of_element_located(
                (By.CLASS_NAME, "svelte-fvoblx"))
        )
        discovers = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "min-h-screen"))
        ).find_elements(By.CLASS_NAME, "carousel")
        list_of_discover = []
        for item in discovers:
            list_of_discover.append(item.text)
    finally:
        pass


def main(wait=True):
    print('Program start')
    test_list = UTIL.extract_file("SkillEnter.csv")
    routines = int(input("Number of test rountines:"))
    for _ in range(routines):
        test_option = random.choice(test_list)
        print(test_option)


if __name__ == "__main__":
    main()
