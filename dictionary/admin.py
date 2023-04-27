from django.contrib import admin
from .models import comesFrom, typeOf, Structure, Correct, Contact
from django import forms

# register all my models here
admin.site.register(comesFrom)
admin.site.register(typeOf)
admin.site.register(Structure)
admin.site.register(Correct)
admin.site.register(Contact)

# Register your models here.
