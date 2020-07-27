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
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(2)

        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()

        following = self._get_names()

        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()

        followers = self._get_names()
        not_following_back = [
            user for user in following if user not in followers]
        print(not_following_back)

    def _get_names(self):
        sleep(4)
        # sugs = self.driver.find_element_by_xpath(
        #     '//h4[contains(text(), Suggestions)]')
        # self.driver.execute_script('arguments[0].scrollIntoView()', sugs)
        # sleep(2)
        scroll_box = self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(2)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")\
            .click()
        return names


my_bot = InstaBot('umar_awan92', pw)
my_bot.get_unfollowers()
