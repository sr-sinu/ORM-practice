'''Import required modules'''
import random
from myapp.models import Colors, People, PeopleAdress
from faker import Faker

fake = Faker()

class FakeData:
    '''Creating random data for use '''
    def __init__(self):
        pass

    def addcolor(self):
        '''creating data for colors'''
        Colors.objects.get_or_create(color_code = fake.color()) 


    def addpeoples(self):
        '''Creating data for peoples'''
        for i in range(100):
            obj = People.objects.create(name = fake.name(), about = fake.text(),
            age = random.randint(11,78), email = fake.email())
            for j in range(0, random.randint(0,30)):
                c, _ = Colors.objects.get_or_create(color_code = fake.color())
                obj.colors.add(c)
                PeopleAdress.objects.create(people = obj, address = fake.address())
