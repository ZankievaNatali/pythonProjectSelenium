class PostPageConsts:
    """Stores constants related to post page"""

    POST_CREATED_MESSAGE_XPATH = ".//div[@class='alert alert-success text-center']"
    POST_CREATED_MESSAGE_TEXT = "New post successfully created."
    POST_UNIQ_XPATH = ".//div/p[text()[contains(.,'Is this post unique')]]"
    POST_UNIQ_TEXT = "Is this post unique? : yes"
    POST_SELECTED_PRIVACY_XPATH = ".//div/p/i/u"
    POST_SELECTED_PRIVACY_ALL_USERS_TEXT = " All Users"
    POST_SELECTED_PRIVACY_PRIVATE_TEXT = " One Person"
    POST_SELECTED_PRIVACY_GROUP_TEXT = " Group Message"
