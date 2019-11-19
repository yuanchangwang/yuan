import random

from django.test import TestCase

# Create your tests here.
from faker import Faker
fake = Faker(locale='zh_CN')

print(random.sample([1, 2, 3, 4], random.randint(1, 4)))