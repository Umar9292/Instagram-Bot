from selenium import webdriver
from time import sleep
from secrets import pw


class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        self.username = username
        sleep(2)

        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(username)

        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(password)

        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]").click()

        sleep(5)

        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button').click()

        sleep(2)

        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[2]').click()

    def get_unfollowers(self):
        self.driver.find_element_by_xpath(
            "//a[contains(@href,'/{}')]".format(self.username)).click()


my_bot = InstaBot('umar_awan92', pw)
