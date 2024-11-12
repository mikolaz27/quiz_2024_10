import time

from celery import shared_task
from django.contrib.auth import get_user_model
from faker.generator import random


@shared_task
def mine_bitcoin():
    time.sleep(random.randint(1, 10))

@shared_task
def normalize_email_task(filter):
    all_users = get_user_model().objects.filter(**filter)

    if all_users:
        for user in all_users:
            print(f'working with user {user.email}')
            user.save()
    else:
        print('empty data')

    return f"Checked {len(all_users)} users"
