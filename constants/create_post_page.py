class CreatePostPageConsts:
    """Stores constants related to post page"""

    TITLE_INPUT_XPATH = ".//input[@id='post-title']"
    BODY_CONTENT_XPATH = ".//textarea[@id='post-body']"
    IS_POST_UNIQ_FLAG_XPATH = ".//input[@name='uniquePost']"
    SELECT_PRIVACY_POST_XPATH = ".//select[@name='select1']"
    SAVE_NEW_POST_BUTTON_XPATH = ".//button[@class='btn btn-primary']"
    POST_SELECTED_PRIVACY_TO_ALL_TEXT = 'Загальнодоступне'
    POST_SELECTED_PRIVACY_TO_GROUP_TEXT = 'Групове повідомлення'
    POST_SELECTED_PRIVACY_TO_PRIVATE_TEXT = 'Приватне повідомлення'
