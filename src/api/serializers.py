from django.contrib.auth import get_user_model
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from quiz.models import Choice, Question, Quiz


class GamerSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "is_staff"]


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = ["id", "text", "is_correct"]


class QuestionSerializer(ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["id", "order_number", "text", "choices"]


class QuizSerializer(ModelSerializer):
    level = CharField(source="get_level_display")

    class Meta:
        model = Quiz
        fields = ["id", "title", "description", "level", "questions_count"]
