import utils as UTIL
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random


def fill_box(skill, driver):
    try:
        textBox = driver.find_element(By.CLASS_NAME, 'addSkills')
        textBox.clear()
        for char in skill:
            textBox.send_keys(char)
        time.sleep(2)
        WebDriverWait(driver, 100).until(
            EC.invisibility_of_element_located(
                (By.CLASS_NAME, "svelte-fvoblx"))
        )
        buttons = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "options")))
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div > button")))
        buttons = buttons.find_elements(By.TAG_NAME, 'button')
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
        ).find_elements(By.LINK_TEXT, "Discover roles based on my skills")[0].click()
        mainScreen = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.CLASS_NAME, "min-h-screen"))
        )
        # TODO: Need to implement a checker to replace input for waiting until all element is loaded
        input("stop here")
        WebDriverWait(driver, 100).until(
            EC.invisibility_of_element_located(
                (By.CLASS_NAME, "svelte-fvoblx"))
        )
        discovers = mainScreen.find_elements(By.CLASS_NAME, "carousel")
        result = UTIL.extract_from_tuple(discovers)
        result.append(not_found)
    except TimeoutException:
        # TODO: Implement a timeout problem notification
        pass
    except NoSuchElementException:
        # TODO: Implement a NoSuchElement problem notification
        pass
    finally:
        return result


def main(wait=True):
    print('Program start')
    test_list = UTIL.extract_file("SkillEnter.csv")
    routines = int(input("Number of test rountines:"))
    url = 'https://careerbrain-uat.herokuapp.com/skills'
    driver = webdriver.Chrome(
        r"/Users/hanle/Documents/Projects/chromedriver")
    driver.get(url)
    for _ in range(routines):
        test_option = random.choice(test_list)
        result = process_skill(test_option, driver)
        print(result)


if __name__ == "__main__":
    main()
