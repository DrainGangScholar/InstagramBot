from selenium import webdriver
from time import sleep


class InstagramBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/")
        sleep(1)
        username_input = self.driver.find_element_by_xpath('//input[@name="username"]')
        username_input.send_keys(username)
        password_input = self.driver.find_element_by_xpath('//input[@name="password"]')
        password_input.send_keys(password)
        login_button = self.driver.find_element_by_xpath('//button[@type="submit"]')
        login_button.click()
        sleep(6)
        not_now_button = self.driver.find_element_by_xpath('//button[text()="Not Now"]')
        not_now_button.click()
        sleep(1)

    def search(self, target):
        search_button = self.driver.find_element_by_xpath('//input[@placeholder="Search"]')
        search_button.send_keys(target)
        sleep(1)
        search_result = self.driver.find_element_by_xpath('//div[@class="fuqBx"]//a[@href="/' + target + '/"]')
        search_result.click()
        sleep(1)

    def unfollow_all(self, username, password, num_followers):
        self.login(username, password)
        self.search(username)
        sleep(1)
        followers_button = self.driver.find_element_by_xpath('//a[@href="/' + username + '/following/"]')
        followers_button.click()
        sleep(2)
        for i in range(num_followers):
            following_button = self.driver.find_element_by_xpath('//button[text()="Following"]')
            following_button.click()
            unfollow_button = self.driver.find_element_by_xpath('//button[text()="Unfollow"]')
            unfollow_button.click()
            sleep(2)

if __name__ == "__main__":
    bot = InstagramBot()
    bot.unfollow_all("your_username", "your_password", 10)
