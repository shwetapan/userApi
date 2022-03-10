from faker import Faker
from appuser.models import AppUser

faker = Faker()

for i in range(70000):
    username= faker.name()
    AppUser(name= username).save()
   


