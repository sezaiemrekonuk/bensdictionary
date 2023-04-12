from django.shortcuts import render
from .models import Structure
from . import searcher

# Create your views here.

def index(request):
    structures = Structure.objects.all()
    context = {
        "structures": structures
    }
    return render(request, 'dictionary/index.html', context)

def search(request):
    context = {}
    if request.method == 'POST':
        context = { 'searchQuery': request.POST.get('search-input') }
    return render(request, 'dictionary/search.html', context)