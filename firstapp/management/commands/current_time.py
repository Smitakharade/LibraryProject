from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.utils import timezone


class Command(BaseCommand):
    ''' Create random users '''
    help = 'Display current time'
    def handle(self, *args, **kwargs):
        print('Hello')
        time = timezone.now()                                           #2023-01-11 00:48:59.032264
        time = timezone.now().strftime('%X')
        print(time)