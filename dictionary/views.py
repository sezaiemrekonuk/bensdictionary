from django.shortcuts import render
from .models import Structure
from . import searcher

# Create your views here.

def index(request):
    return render(request, 'dictionary/index.html')

def search(request):   
    if request.method == 'POST':
        searchInput = request.POST.get('search-input')
        searchType = request.POST.get('search-type')
        
        if searchType == 'Tüm Türler':
            context = { 'searchQuery': searchInput, 'searchResults': searcher.searcher(searchInput) }
        else:
            context = { 'searchQuery': searchInput, 'searchResults': searcher.searcher(searchInput, searchType) }
            
        return render(request, 'dictionary/search.html', context)
    
    else:
        return render(request, 'dictionary/index.html')