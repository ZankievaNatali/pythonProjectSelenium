"""Test related to registration form and process"""
import logging
import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:
    """Stores test for registration form base functionality"""
    log = logging.getLogger("[StartPage]")

    @staticmethod
    def random_num():
        """Generates random number"""
        return str(random.randint(111111, 999999))

    @staticmethod
    def random_str(length=5):
        """Generates random string"""
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def test_incorrect_login(self):
        """
        - Pre-condition:
            -Open start page
        -Steps:
            -Fill login
            -Fill Password
            -Click on SignIn button
            -Verify error
        """
        # open start page
        driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
        driver.get("https://qa-complexapp.onrender.com/")
        self.log.info("Start page was opened")
        time.sleep(1)

        # Fill in Login
        login_field = driver.find_element(By.XPATH, ".//input[@placeholder='Username']")
        login_field.clear()
        login_field.send_keys("testuser1234")
        self.log.info("Login was filled")
        time.sleep(1)

        # Fill in password
        password_field = driver.find_element(By.XPATH,
                                             ".//input[@name='password'][@class='form-control form-control-sm "
                                             "input-dark']")
        password_field.clear()
        password_field.send_keys("testuser1234")
        self.log.info("Password was filled")
        time.sleep(1)

        # Click on SignIn button
        sign_in = driver.find_element(By.XPATH, ".//button[text()='Sing In']")
        sign_in.click()
        self.log.info("Sign in was clicked")
        time.sleep(1)

        # Verify error
        error_message = driver.find_element(By.XPATH, ".//div[@class='alert alert-danger text-center']")
        assert error_message.text == 'Error'
        driver.close()

    def test_empty_login(self):
        """
        - Pre-condition:
            -Open start page
        -Steps:
            -Fill login
            -Fill Password
            -Click on SignIn button
            -Verify error
        """
        # open start page
        driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
        driver.get("https://qa-complexapp.onrender.com/")
        self.log.info("Start page was opened")
        time.sleep(1)

        # Fill in Login
        login_field = driver.find_element(By.XPATH, ".//input[@placeholder='Username']")
        login_field.clear()
        login_field.send_keys("")
        self.log.info("Login was filled")
        time.sleep(1)

        # Fill in password
        password_field = driver.find_element(By.XPATH,
                                             ".//input[@name='password'][@class='form-control form-control-sm "
                                             "input-dark']")
        password_field.clear()
        password_field.send_keys("")
        self.log.info("Password was filled")
        time.sleep(1)

        # Click on SignIn button
        sign_in = driver.find_element(By.XPATH, ".//button[text()='Sing In']")
        sign_in.click()
        self.log.info("Sign in was clicked")
        time.sleep(1)

        # Verify error
        error_message = driver.find_element(By.XPATH, ".//div[@class='alert alert-danger text-center']")
        assert error_message.text == 'Error'
        driver.close()

    def test_registration_form(self):
        """
        - Pre-condition:
            -Open start page, registration form
        -Steps:
            -Fill username
            -Fill email address
            -Fill Password
            -Click on "Sign Up for OurApp" button
            -Verify transfer to personal page
        """

        # open start page
        driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
        driver.get("https://qa-complexapp.onrender.com/")
        self.log.info("Start page was opened")
        time.sleep(1)

        # Fill in Login
        username_field = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        username_field.clear()
        username = f"testuser{self.random_num()}"
        username_field.send_keys(username)
        time.sleep(1)
        self.log.info("Username was filled")

        # Fill in email
        email_field = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email_field.clear()
        email_field.send_keys(f"{username}@user.com")
        self.log.info("Email was filled")
        time.sleep(1)

        # Fill in password
        password_field = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password_field.clear()
        password_field.send_keys(f"pass{username}")
        self.log.info("Password was filled")
        time.sleep(1)

        # Click on Sign Up button
        sign_up = driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']")
        sign_up.click()
        self.log.info("Sign Up was clicked")
        time.sleep(4)

        # Verify transfer to personal page
        page_title = driver.find_element(by=By.XPATH, value=f".//span[text()=' {username}']")
        assert page_title.text == username
        self.log.info("Transfer  to personal page (registration) was verified")
        driver.close()

    def test_invalid_reg_username(self):
        """
        - Pre-condition:
            -Open start page, registration form
        -Steps:
            -Fill in already registered username
            -Verify error
        """

        # open start page
        driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
        driver.get("https://qa-complexapp.onrender.com/")
        self.log.info("Start page was opened")
        time.sleep(1)

        # Fill in Login
        username_field = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        username_field.clear()
        username = "test1"
        username_field.send_keys(username)
        time.sleep(2)
        self.log.info("Username was filled")

        # Verify transfer to personal page
        page_title = driver.find_element(by=By.XPATH, value="//div[@class='form-group']/div[text()='That username is "
                                                            "already taken.']")
        assert page_title.text == "That username is already taken."
        self.log.info("Error with already existing username was verified")
        driver.close()

    def test_invalid_reg_email(self):
        """
        - Pre-condition:
            -Open start page, registration form
        -Steps:
            -Fill in the username
            -Fill in email that already being used
            -Verify error
        """

        # open start page
        driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
        driver.get("https://qa-complexapp.onrender.com/")
        self.log.info("Start page was opened")
        time.sleep(1)

        # Fill in Login
        username_field = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        username_field.clear()
        username = "test1"
        username_field.send_keys(username)
        time.sleep(1)
        self.log.info("Username was filled")

        # Fill in email
        email_field = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email_field.clear()
        email_field.send_keys("test@test.com")
        self.log.info("Email was filled")
        time.sleep(2)

        # Verify transfer to personal page
        page_title = driver.find_element(by=By.XPATH, value="//div[@class='form-group']/div[text()='That email is "
                                                            "already being used.']")
        assert page_title.text == "That email is already being used."
        self.log.info("Error with already existing email was verified")
        driver.close()

    def test_invalid_reg_pass_len(self):
        """
        - Pre-condition:
            -Open start page, registration form
        -Steps:
            -Fill in the username
            -Fill in email address
            -Fill in Password with more than 50 symbols
            -Verify error
        """

        # open start page
        driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
        driver.get("https://qa-complexapp.onrender.com/")
        self.log.info("Start page was opened")
        time.sleep(1)

        # Fill in Login
        username_field = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        username_field.clear()
        username = f"testuser{self.random_num()}"
        username_field.send_keys(username)
        time.sleep(1)
        self.log.info("Username was filled")

        # Fill in email
        email_field = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email_field.clear()
        email_field.send_keys(f"{username}@user.com")
        self.log.info("Email was filled")
        time.sleep(1)

        # Fill in password
        password_field = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password_field.clear()
        password = ''.join([str(x) for x in range(31)])
        password_field.send_keys(password)
        self.log.info("Password was filled")
        time.sleep(2)

        # Verify transfer to personal page
        page_title = driver.find_element(by=By.XPATH, value="//div[@class='form-group']/div[text()='Password cannot "
                                                            "exceed 50 characters.']")
        assert page_title.text == "Password cannot exceed 50 characters."
        self.log.info("Error with Password length was verified")
        driver.close()
