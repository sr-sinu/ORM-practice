from django.contrib import admin
from myapp.models import YoutubeVideo,Colors,People,PeopleAdress
# Register your models here.

admin.site.register(YoutubeVideo)
admin.site.register(Colors)
admin.site.register(People)
admin.site.register(PeopleAdress)
