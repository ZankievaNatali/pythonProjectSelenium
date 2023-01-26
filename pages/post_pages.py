import logging

from constants.post_page import PostPageConsts
from pages.base_page import BasePage


class PostPage(BasePage):
    """Stores methods describes post page options"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = PostPageConsts
        self.log = logging.getLogger("[PostPage]")

    def verify_post_created(self):
        """Verify post creating message"""
        assert self.compare_element_text(xpath=self.const.POST_CREATED_MESSAGE_XPATH,
                                         text=self.const.POST_CREATED_MESSAGE_TEXT)

    def verify_if_post_uniq(self):
        """Verify if post uniq message"""
        assert self.compare_element_text(xpath=self.const.POST_UNIQ_XPATH,
                                         text=self.const.POST_UNIQ_TEXT)

    def verify_selected_privacy(self, value):
        """Verify if privacy matches in created post"""
        accordance_post_select_value = {"Загальнодоступне": "All Users", "Групове повідомлення": "Group Message",
                                        "Приватне повідомлення": "One Person"}
        text = accordance_post_select_value[value]
        assert self.compare_element_text(xpath=self.const.POST_SELECTED_PRIVACY_XPATH,
                                         text=text)
