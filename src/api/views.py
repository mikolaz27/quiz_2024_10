from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from api.serializers import GamerSerializer, QuestionSerializer, QuizSerializer
from quiz.models import Question, Quiz


class GamerViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = GamerSerializer


class QuestionDetailView(RetrieveAPIView):
    serializer_class = QuestionSerializer

    def get_object(self):
        return Question.objects.get(quiz_id=self.kwargs.get("pk"), order_number=self.kwargs.get("order"))


class QuizListView(ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
