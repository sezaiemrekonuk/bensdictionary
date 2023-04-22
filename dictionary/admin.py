from django.contrib import admin
from .models import comesFrom, typeOf, Structure, Correct

# register all my models here
admin.site.register(comesFrom)
admin.site.register(typeOf)
admin.site.register(Structure)
admin.site.register(Correct)
# Register your models here.
