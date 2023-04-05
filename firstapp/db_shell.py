from django.contrib.auth.models import User, Group
from django.utils.crypto import get_random_string


print(User.objects.all())

# User.objects.create_user(username='smita', password='Smita@123', email='smita@gmail.com')

print(get_random_string())          # this will return a random str of length 12 we can also chage that param as per requirement
# print(get_random_string(5, 'A-Z,a-z,0-9,!@#$%^&*'))