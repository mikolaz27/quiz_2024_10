from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api.views import GamerViewSet, QuestionDetailView, QuizListView

app_name = "api"

router = routers.DefaultRouter()
router.register("gamers", GamerViewSet)

# POST gamers/
# GET gamers/
# GET gamers/<id>/
# PUT gamers/<id>/
# PATCH gamers/<id>/
# DELETE gamers/<id>/

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", include(router.urls)),
    path("docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("quiz/<int:pk>/question/<int:order>/", QuestionDetailView.as_view(), name="question_details"),
    path("quiz/", QuizListView.as_view(), name="quiz_list"),
    path("auth/", include("djoser.urls.jwt")),
]
