from django.contrib import admin
from .models import comesFrom, typeOf, Structure

# register all my models here
admin.site.register(comesFrom)
admin.site.register(typeOf)
admin.site.register(Structure)

# Register your models here.
