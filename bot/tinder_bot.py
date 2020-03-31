from selenium import webdriver
from time import sleep
from secrets import email, password


class TinderBot:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(5)

        self.open_facebook_login_popup()
        self.driver.switch_to.window(self.submit_login_form())

        sleep(4)

        self.accept_tinder_permissions()

    def open_facebook_login_popup(self):
        login_btn = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')

        if login_btn.text == 'LOGIN WITH FACEBOOK':
            login_btn.click()
        elif login_btn.text == 'LOG IN WITH PHONE NUMBER':
            more_opts = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
            more_opts.click()
            fb_login_btn = self.driver.find_element_by_xpath(
                '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button')
            fb_login_btn.click()
        else:
            return 'ERROR COULD NOT LOG IN'

    def submit_login_form(self):
        # Switching to the popup log in window
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_elem = self.driver.find_element_by_xpath('//*[@id="email"]')
        password_elem = self.driver.find_element_by_xpath('//*[@id="pass"]')

        email_elem.send_keys(email)
        password_elem.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()
        return base_window

    def accept_tinder_permissions(self):
        enable_loc = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        enable_loc.click()

        enable_not = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        enable_not.click()

        exit_cookie_consent = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/button')
        exit_cookie_consent.click()

        sleep(6)

        close_passport_popup = bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
        close_passport_popup.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def auto_like(self):
        while True:
            try:
                self.like()
            except Exception:
                try:
                    self.close_match()
                except Exception:
                    self.close_popup()

    def close_match(self):
        close_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        close_btn.click()

    def close_popup(self):
        '//*[@id="modal-manager"]/div/div/div[3]/button[2]'
        close_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        close_btn.click()


bot = TinderBot()
bot.login()
bot.auto_like()
