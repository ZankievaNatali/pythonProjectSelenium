class StartPageConst:
    """Stores constants related to start page"""

    # Sign in
    SIGN_IN_USERNAME_FIELD_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_FIELD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_TEXT = "Sign In"
    SIGN_IN_BUTTON_XPATH = f".//button[text()='{SIGN_IN_BUTTON_TEXT}']"
    SIGN_IN_ERROR_TEXT = "Invalid username pasword"
    SIGN_IN_ERROR_XPATH = ".//div[@class='alert alert-danger text-center']"

    # Sign up
    SIGN_UP_USERNAME_FIELD_XPATH = ".//input[@id='username-register']"
    SIGN_UP_EMAIL_FIELD_XPATH = ".//input[@id='email-register']"
    SIGN_UP_PASSWORD_XPATH = ".//input[@id='password-register']"
    SIGN_UP_BUTTON_XPATH = ".//button[text()='Sign up for OurApp']"
    SIGN_UP_ERROR_TEXT_USERNAME = 'That username is already taken.'
    SIGN_UP_ERROR_TEXT_USERNAME_INV_SYMB = 'Username can only contain letters and numbers.'
    SIGN_UP_ERROR_TEXT_EMAIL = 'That email is already being used.'
    SIGN_UP_ERROR_TEXT_PASSWORD = 'Password cannot exceed 50 characters.'
    SIGN_UP_ERROR_USERNAME_XPATH = f"//div[@class='form-group']/div[text()= '{SIGN_UP_ERROR_TEXT_USERNAME}']"
    SIGN_UP_ERROR_USERNAME_INV_SYMB_XPATH = f"//div[@class='form-group']/div[text()= '{SIGN_UP_ERROR_TEXT_USERNAME_INV_SYMB}']"
    SIGN_UP_ERROR_EMAIL_XPATH = f"//div[@class='form-group']/div[text()= '{SIGN_UP_ERROR_TEXT_EMAIL}']"
    SIGN_UP_ERROR_PASSWORD_XPATH = f"//div[@class='form-group']/div[text()= '{SIGN_UP_ERROR_TEXT_PASSWORD}']"
