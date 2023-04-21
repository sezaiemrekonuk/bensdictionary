from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('search', views.search, name='search'),
    path('search/<slug:slug>', views.slugSearch, name='slugSearch'),
    path('about', views.about, name='about'),
    path('correct/<slug:slug>', views.correct, name='correct'),
]