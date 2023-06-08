class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.username_locator = (By.NAME, 'email')
        self.password_locator = (By.NAME, 'password')
        self.login_button_locator = (By.XPATH, '//button[contains(text(),"Login)]')

    def enter_username(self, username):
        self.driver.find_element(self.username_locator).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(self.password_locator).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(self.login_button_locator).click()

