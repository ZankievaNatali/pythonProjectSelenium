"""Test related to registration form and process"""
import logging

from pages.utils import random_num, random_str


class TestStartPage:
    """Stores test for registration form base functionality"""
    log = logging.getLogger("TestStartPage]")

    def test_valid_login(self, start_page):
        """
        - Pre-condition:
            -Open start page
        -Steps:
            -Fill in valid login
            -Fill in valid Password
            -Click on Sign In button
            -Verify success message
        """
        # Prepare test data
        username = "tester"
        password = "1234567891011"

        # Login as valid username
        hello_page = start_page.sign_in(username, password)
        self.log.info("Logged in as valid username")

        # Verify transfer to Hello page
        hello_page.verify_success_sign_in(username=username)
        self.log.info("Sign in for user '%s' was success and verified", username)

    def test_invalid_login(self, start_page):
        """
        - Pre-condition:
            -Open start page
        -Steps:
            -Fill in login
            -Fill in wrong Password
            -Click on SignIn button
            -Verify error
        """
        # Login as invalid username
        start_page.sign_in("test", "test1")
        self.log.info("Logged in as invalid username")

        # Verify error
        start_page.verify_sign_in_error()
        self.log.info("Error message was verified")

    def test_empty_login(self, start_page):
        """
        - Pre-condition:
            -Open start page
        -Steps:
            -Fill in empty login
            -Fill in empty Password
            -Click on SignIn button
            -Verify error
        """
        # Login with empty username and password
        start_page.sign_in("", "")
        self.log.info("Logged in with empty username and password")

        # Verify error
        start_page.verify_sign_in_error()
        self.log.info("Error message was verified")

    def test_registration_form(self, start_page):
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
        # Prepare test data
        username = f"userrandomtest{random_num()}"
        email = f"{username}@user.com"
        password = f"password{username}"

        # Fill in username, email, password
        hello_page = start_page.sign_up(username=username, email=email, password=password)
        self.log.info("User was registered")

        # Verify transfer to Hello page
        hello_page.verify_sign_up_message(username=username)
        self.log.info("Registration for user '%s' was success and verified", username)

    def test_existing_reg_username(self, start_page):
        """
        - Pre-condition:
            -Open start page, registration form
        -Steps:
            -Fill in already registered username
            -Verify error
        """
        # Prepare test data
        username = "test"
        email = f"{random_str()}@user.com"
        password = f"password{username}"

        # Fill in username
        start_page.sign_up(username=username, email=email, password=password, verify=False)
        self.log.info("Existing username was filled in")

        # Verify transfer to personal page
        start_page.verify_sign_up_error()
        self.log.info("Error with already existing username was verified")

    def test_invalid_symbol_reg_username(self, start_page):
        """
        - Pre-condition:
            -Open start page, registration form
        -Steps:
            -Fill in username with invalid symbols
            -Verify error
        """
        # Prepare test data
        username = "test_user!={"
        email = f"{username}@user.com"
        password = f"pass{username}"

        # Fill in fields
        start_page.sign_up(username=username, email=email, password=password, verify=False)
        self.log.info("Username with invalid symbols was filled in")

        # Verify error
        start_page.verify_sign_up_error()
        self.log.info("Error about invalid symbols in username was verified")

    def test_existing_reg_email(self, start_page):
        """
        - Pre-condition:
            -Open start page, registration form
        -Steps:
            -Fill in the username
            -Fill in email that already being used
            -Verify error
        """

        # Prepare test data
        username = f"{random_str()}{random_num()}"
        email = "test@test.com"
        password = f"pass{username}"

        # Fill in fields
        start_page.sign_up(username=username, email=email, password=password, verify=False)
        self.log.info("Existing email was filled in")

        # Verify error
        start_page.verify_sign_up_error()
        self.log.info("Error with already existing email was verified")

    def test_invalid_len_reg_pass_len(self, start_page):
        """
        - Pre-condition:
            -Open start page, registration form
        -Steps:
            -Fill in the username
            -Fill in email address
            -Fill in Password with more than 50 symbols
            -Verify error
        """

        # Prepare test data
        username = f"{random_str()}{random_num()}"
        email = f"{username}@user.com"
        password = ''.join([str(x) for x in range(31)])

        # Fill in fields
        start_page.sign_up(username=username, email=email, password=password, verify=False)
        self.log.info("Password with over length was filled in")

        # Verify error
        start_page.verify_sign_up_error()
        self.log.info("Error with Password length was verified")
