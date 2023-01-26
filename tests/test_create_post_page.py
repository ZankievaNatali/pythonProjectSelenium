"""Test related to creation post page"""
import logging

import pytest

from constants.create_post_page import CreatePostPageConsts
from pages.utils import random_num, random_str, select


class TestCreatePostPage:
    """Stores test for create post page base functionality"""
    log = logging.getLogger("[TestCreatePostPage]")

    def test_create_post(self, start_page):
        """
                - Pre-condition:
                    -Sign up as a user
                    -Navigate to create post page
                -Steps:
                    -Create post by filling title and body
                    -Verify the success message
                """
        # Sign Up as a user
        username = f"userrandomtest{random_num()}"
        email = f"{username}@user.com"
        password = f"password{username}"
        hello_page = start_page.sign_up(username=username, email=email, password=password)
        self.log.info("User was registered")

        # Navigate to create post page
        create_post_page = hello_page.navigate_to_create_post()
        self.log.info("Navigated to creation post page")

        # Create post by filling title and body
        title = " ".join(random_str() for _ in range(4))
        body = " ".join(random_str() for _ in range(50))
        post_page = create_post_page.create_post(title=title, body=body)
        self.log.info("Post created")

        # Verify the success message
        post_page.verify_post_created()
        self.log.info("Message was verify")

    def test_if_post_uniq(self, start_page):
        """
            - Pre-condition:
                -Sign in as a registered user
                -Navigate to create post page
            -Steps:
                -Select the flag "Is this post unique?"
                -Create post by filling title and body
                -Verify the message if the message is uniq
        """
        # Prepare test data
        username = "tester"
        password = "1234567891011"

        # Login as valid username
        hello_page = start_page.sign_in(username, password)
        self.log.info("Logged in as valid username")

        # Navigate to create post page
        create_post_page = hello_page.navigate_to_create_post()
        self.log.info("Navigated to creation post page")

        # Create post by filling title and body
        title = " ".join(random_str() for _ in range(4))
        body = " ".join(random_str() for _ in range(50))
        post_page = create_post_page.create_post(title=title, body=body, uniq_flag=True)
        self.log.info("Post created")

        # Verify the success message
        post_page.verify_if_post_uniq()
        self.log.info("Post is uniq")

    @pytest.mark.parametrize('execution_number', range(len(select(arg=CreatePostPageConsts,
                                                                  pattern='POST_SELECTED_PRIVACY'))))
    def test_post_privacy(self, execution_number, start_page):
        """
        Run the test as many times as values in post privacy selection, cover all privacy post settings
            - Pre-condition:
                -Sign in as a registered user
                -Navigate to create post page
            -Steps:
                -Select post privacy level (one of existing)
                -Create post by filling title and body
                -Verify the message if the privacy is matched
        """
        assert True
        # Prepare test data
        username = "tester"
        password = "1234567891011"
        privacy = select(arg=CreatePostPageConsts, pattern='POST_SELECTED_PRIVACY')

        # Login as valid username
        hello_page = start_page.sign_in(username, password)
        self.log.info("Logged in as valid username")

        # Navigate to create post page
        create_post_page = hello_page.navigate_to_create_post()
        self.log.info("Navigated to creation post page")

        # Create post by filling title and body
        title = " ".join(random_str() for _ in range(4))
        body = " ".join(random_str() for _ in range(50))
        post_page = create_post_page.create_post(title=title, body=body, privacy_value=privacy[execution_number])
        self.log.info("Post created with privacy %s", privacy[execution_number])

        # Verify the success message
        post_page.verify_selected_privacy(value=privacy[execution_number])
        self.log.info("Privacy %s was verified on post page", privacy[execution_number])
