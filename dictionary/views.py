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
        if (len(searcher.searcher(searchInput)) != 0):
            if searchType == 'Tüm Türler':
                result = searcher.searcher(searchInput)[0]
                downSide = [Structure.get.filter(id=obj).slug for obj in range(result.id, result.id)]
                
                if (result.id <= 5 or not Structure.get.filter(id=result.id) == None):
                    topSide = [Structure.get.filter(id=obj).slug for obj in range(result.id, result.id)]
                else:
                    topSide = [Structure.get.filter(id=obj).slug for obj in range(result.id, result.id)]
                    
                
                context = { 'searchQuery': searchInput, 'searchResults': result, 'topSide': topSide, 'downSide': downSide }
            else:
                result = searcher.searcher(searchInput, searchType)[0]
                downSide = [Structure.get.filter(id=obj).slug for obj in range(result.id, result.id)]
                
                if (result.id <= 5 or not Structure.get.filter(id=result.id) == None):
                    topSide = [Structure.get.filter(id=obj).slug for obj in range(result.id, result.id)]
                else:
                    topSide = [Structure.get.filter(id=obj).slug for obj in range(result.id, result.id)]
                    
                
                context = { 'searchQuery': searchInput, 'searchResults': result, 'topSide': topSide, 'downSide': downSide }
                
            return render(request, 'dictionary/search.html', context)

        else:
            return render(request, 'dictionary/about.html')

        
    else:
        return render(request, 'dictionary/index.html')