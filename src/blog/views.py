from IPython.core.release import author
from django.http import HttpRequest, HttpResponse
from faker import Faker
from faker.generator import random

from blog.models import Entity, Blog


def create_blog(request):
    faker = Faker("UK")

    saves_data = Entity(
        blog=[Blog(name=faker.word(), text=faker.paragraph(nb_sentences=5),
                   author=faker.first_name(), rating=random.randint(1, 10)) for _ in range(5)],
        headline=faker.paragraph(nb_sentences=1)
    ).save()

    return HttpResponse(f"Done: {saves_data}")


def all_blogs(request):
    blogs = Entity.objects.all()

    print(blogs)

    return HttpResponse(f"Done: {[blog.headline for blog in blogs]}")
