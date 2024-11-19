from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CASCADE

from accounts.models import BaseModel


class LEVEL_CHOICES(models.IntegerChoices):
    BASIC = 0, "Basic"
    MEDIUM = 1, "Medium"
    ADVANCED = 2, "Advanced"


class Category(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="img/category/covers", null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name} ({self.pk})"


class Quiz(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024, blank=True, null=True)
    image = models.ImageField(upload_to="img/quiz/covers", default="default.png", null=True, blank=True)
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES.choices, default=LEVEL_CHOICES.BASIC)
    category = models.ForeignKey("quiz.Category", related_name="quizzes", on_delete=CASCADE)

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return f"{self.title} ({self.pk})"

    def questions_count(self):
        return self.questions.count()


class Result(BaseModel):
    quiz = models.ForeignKey("quiz.Quiz", related_name="results", on_delete=CASCADE)
    user = models.ForeignKey(get_user_model(), related_name="results", on_delete=CASCADE)
    count_of_correct_answers = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.user.email}_{self.quiz.title} ({self.pk})"


class Question(BaseModel):
    quiz = models.ForeignKey("quiz.Quiz", related_name="questions", on_delete=CASCADE)
    text = models.CharField(max_length=512)
    order_number = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.text} ({self.pk})"


class Choice(BaseModel):
    question = models.ForeignKey("quiz.Question", related_name="choices", on_delete=CASCADE)
    text = models.CharField(max_length=512)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}_{self.question.order_number} ({self.pk})"
