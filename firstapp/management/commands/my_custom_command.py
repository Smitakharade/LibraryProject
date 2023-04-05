from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.utils import timezone


class Command(BaseCommand):
    ''' Create random users '''
    help = 'Display current time'
    def add_arguments(self, parser) -> None:
        parser.add_argument('total', type=int, help='indicates no of users to be created')
    
    def handle(self, *args, **kwargs):
        total = kwargs['total']
        # print(kwargs)
        for i in range(total):
            User.objects.create_user(username=get_random_string(), password='Admin@123', email='')



class Command(BaseCommand):
    ''' Generate random user '''
    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='creates a random users')

    def handle(self, *args, **kwargs):
        total =  kwargs['total']
        for i in range(total):
            User.objects.create_user(username=get_random_string(), password="123", email='')        
