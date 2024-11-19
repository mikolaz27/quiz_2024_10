import unittest
from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class TestAuthGamer(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = get_user_model()(email="gamer@example.com")
        self.user.set_password("12345678")
        self.user.save()

        self.manager = get_user_model()(email="manager@example.com", is_staff=True)
        self.manager.set_password("12345678")
        self.manager.save()

    def test_user_login_wrong_email(self):
        user_login = self.client.login(email="wrong_email", password="12345678")
        self.assertFalse(user_login)

    def test_user_login_wrong_password(self):
        user_login = self.client.login(email="gamer@example.com", password="wrong_password")
        self.assertFalse(user_login)

    def test_user_access_admin_panel(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_manager_access_admin_panel(self):
        self.client.force_login(self.manager)
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @unittest.skip("We dont have index page, will have it in week/spint 35")
    def test_user_access_index_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    @unittest.expectedFailure
    def test_manager_access_admin_panel_failure_expected(self):
        self.client.force_login(self.manager)
        response = self.client.get(reverse("admin:index"))
        self.assertEqual(response.status_code, HTTPStatus.IM_A_TEAPOT)
