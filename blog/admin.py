from django.contrib import admin

# Register your models here.

from blog.models import *

admin.site.register(Proyecto)
admin.site.register(Tarea)