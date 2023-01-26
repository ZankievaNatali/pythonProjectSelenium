import logging

from constants.create_post_page import CreatePostPageConsts
from pages.base_page import BasePage


class CreatePostPage(BasePage):
    """Stores methods describes start page options"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = CreatePostPageConsts
        self.log = logging.getLogger("[CreatePostPage]")

    def create_post(self, title, body, privacy_value="Загальнодоступне", uniq_flag=False):
        """Create post using provided values"""

        # Fill in fields
        self.fill_field(xpath=self.const.TITLE_INPUT_XPATH, value=title)
        self.fill_field(xpath=self.const.BODY_CONTENT_XPATH, value=body)
        self.select(xpath=self.const.SELECT_PRIVACY_POST_XPATH, value=privacy_value)
        if uniq_flag:
            self.click(xpath=self.const.IS_POST_UNIQ_FLAG_XPATH)
        self.click(xpath=self.const.SAVE_NEW_POST_BUTTON_XPATH)

        from pages.post_pages import PostPage
        return PostPage(self.driver)
