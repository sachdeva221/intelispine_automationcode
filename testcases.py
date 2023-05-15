from selenium.webdriver.common.by import By


class Login:
    def __init__(self, Driver):
        self.Driver = Driver

    email = (By.XPATH, "//input[@type='email']")
    enterpwd = (By.ID, "password")
    clickonlogin = (By.CSS_SELECTOR, ".btn")



    def loginemail(self):
        return self.Driver.find_element(*Login.email)

    def enter_pawd(self):
        return self.Driver.find_element(*Login.enterpwd)

    def click_to_login(self):
        return self.Driver.find_element(*Login.clickonlogin)








