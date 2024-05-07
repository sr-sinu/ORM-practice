'''import required modules'''
import uuid
from django.db import models


class YoutubeVideo(models.Model):
    '''Data sending to youtube'''
    video = models.FileField(upload_to='youtube')

class BaseModel(models.Model):
    '''Base model for reference'''
    uid = models.UUIDField(default = uuid.uuid4,primary_key = True, editable = True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        '''making abstract table'''
        abstract = True

class Colors(BaseModel):
    '''Creating Colors table'''
    color_code = models.CharField(max_length=100)

class People(models.Model):
    '''Creating People table'''
    name = models.CharField(max_length=100)
    about = models.TextField()
    age = models.IntegerField()
    email = models.EmailField()
    colors = models.ManyToManyField(Colors)

class PeopleAdress(BaseModel):
    '''People address '''
    people= models.ForeignKey(People, on_delete=models.CASCADE, related_name='adress')
    address = models.TextField()
