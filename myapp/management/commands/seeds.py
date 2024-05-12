'''Import required modules'''
import random
from myapp.models import Colors, People, PeopleAdress
from faker import Faker
from django.core.management.base import BaseCommand

fake = Faker()

class Command(BaseCommand):
    '''Creating random data for use '''

    help = "Creating Fake Data For Tasting"
    
    def handle(self, *args, **kwrgs):
        # def addcolor():
        '''creating data for colors'''
        Colors.objects.get_or_create(color_code = fake.color()) 
        # def addpeoples():
        '''Creating data for peoples'''
        for i in range(100):
            obj = People.objects.create(name = fake.name(), about = fake.text(),
            age = random.randint(11,78), email = fake.email())
            for j in range(0, random.randint(0,30)):
                c, _ = Colors.objects.get_or_create(color_code = fake.color())
                obj.colors.add(c)
                PeopleAdress.objects.create(people = obj, address = fake.address())
        self.stdout.write(self.style.SUCCESS("Command excuted successfully.....!"))