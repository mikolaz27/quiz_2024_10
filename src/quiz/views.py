from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse

from quiz.tasks import mine_bitcoin, normalize_email_task


def bitcoin(request:HttpRequest)->HttpResponse:
    mine_bitcoin.delay()
    return HttpResponse("Task is started")

def normalize_email(request:HttpRequest)->HttpResponse:
    normalize_email_task.delay(filter={"email__endswith":".com"})
    return HttpResponse("Task is started")