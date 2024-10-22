import unittest
from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.exceptions import ErrorDetail
from rest_framework.status import (HTTP_200_OK, HTTP_401_UNAUTHORIZED,
                                   HTTP_403_FORBIDDEN)
from rest_framework.test import APIClient

from quiz.utils.samples import sample_question, sample_quiz


class TestApi(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.quiz = sample_quiz(level=1, title="Test", description="Some description")
        self.question = sample_question(quiz=self.quiz, order_number=1)

        self.user = get_user_model()(email="user@example.com")
        self.user.set_password("qwerty1234")
        self.user.save()

    def test_question_details_no_access(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse("api:question_details", kwargs={"pk": self.quiz.pk, "order": self.question.order_number})
        )

        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)
        self.assertEqual(
            response.data,
            {
                "detail": ErrorDetail(
                    string="You do not have permission to perform this action.", code="permission_denied"
                )
            },
        )

    def test_question_details(self):
        self.user.is_superuser = True
        self.user.save()

        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse("api:question_details", kwargs={"pk": self.quiz.pk, "order": self.question.order_number})
        )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, {"id": 1, "order_number": 1, "text": "Text for testing", "choices": []})

    @unittest.expectedFailure
    def test_quiz_list_no_access(self):
        response = self.client.get(reverse("api:quiz_list"))
        self.assertEqual(response.data, HTTP_401_UNAUTHORIZED)

    def test_quiz_list(self):
        response = self.client.get(reverse("api:quiz_list"))

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(
            response.data,
            [{"id": 1, "title": "Test", "description": "Some description", "level": "Medium", "questions_count": 1}],
        )
