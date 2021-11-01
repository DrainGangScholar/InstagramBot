from selenium import webdriver
from time import sleep



class InstagramBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        sleep(0.5)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/")
        sleep(0.5)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
        sleep(0.5)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
        sleep(0.5)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]").click()
        sleep(6)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/div/div/div/button").click()
        sleep(8)
        self.driver.find_element_by_xpath(
            '//button[text()="Not Now"]').click()
        sleep(1)

    def search(self, target):
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div/span[2]").click()
        sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(target)
        sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div").click()
        sleep(1)

    def unfollowAll(self, username, password, numOfFollowers):
        self.login(username, password)
        self.search(username)
        sleep(0.5)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
        sleep(2)
        for i in range(numOfFollowers):
            self.driver.find_element_by_xpath('//button[text()="Following"]').click()
            self.driver.find_element_by_xpath('//button[text()="Unfollow"]').click()
            sleep(2)


