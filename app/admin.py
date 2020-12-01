from django.contrib import admin

# Register your models here.

from app.models import *

admin.site.register(UserProfile)






#python manage.py makemigrations
#python manage.py migrate