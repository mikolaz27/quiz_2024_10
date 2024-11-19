from django.core.exceptions import ValidationError
from django.test import TestCase

from quiz.models import Quiz
from quiz.utils.samples import sample_question, sample_quiz


class TestQuiz(TestCase):
    def setUp(self):
        self.test_quiz = sample_quiz(
            title="Test Quiz",
        )
        self.questions_count = 5
        for order_number in range(1, self.questions_count + 1):
            sample_question(quiz=self.test_quiz, order_number=order_number)

    def test_questions_count(self):
        self.assertEqual(self.questions_count, self.test_quiz.questions_count())

    def test_quiz_title_limit(self):
        with self.assertRaises(ValidationError):
            sample_quiz(title="A" * 5000)

        self.assertEqual(Quiz.objects.count(), 1)
