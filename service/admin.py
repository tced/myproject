from django.contrib import admin

# Register your models here.
from .models import Users

#grabbing database, Users, so we have access to it
admin.site.register(Users)