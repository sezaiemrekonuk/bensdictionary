from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Structure
from . import searcher

# Create your views here.

def index(request):
    return render(request, 'dictionary/index.html')

def search(request):   
    if request.method == 'POST':
        print(request.session.get('FROMSLUG'))
        searchInput = request.POST.get('search-input')
        searchType = request.POST.get('search-type')
        searchResult = None
        try:
            searchResult = searcher.searcher(searchInput, searchType)[0]
        except:
            return render(request, 'dictionary/search.html', {'searchInput': searchInput, 'searchType': searchType, 'searchResult': searchResult, 'noResult': True})
        resultId = searchResult.id
        lowerList = []
        upperList = []
        for i in range(resultId + 1, resultId + 6):
            try:
                lowerList.append(Structure.objects.get(id=i))
            except:
                break
        if resultId - 5 < 0:
            for i in range(1, resultId):
                try:
                    upperList.append(Structure.objects.get(id=i))
                except:
                    break
        else:
            for i in range(resultId - 5, resultId):
                try:
                    upperList.append(Structure.objects.get(id=i))
                except:
                    break
        return render(request, 'dictionary/search.html', {'searchInput': searchInput, 'searchType': searchType, 'searchResult': searchResult, 'lowerList': lowerList, 'upperList': upperList, 'noResult': False})
    else:
        searchInput = request.POST.get('search-input')
        searchType = request.POST.get('search-type')
        searchResult = request.session.get('SEARCHRESULT')
        resultId = searchResult.id
        lowerList = []
        upperList = []
        for i in range(resultId + 1, resultId + 6):
            try:
                lowerList.append(Structure.objects.get(id=i))
            except:
                break
        if resultId - 5 < 0:
            for i in range(1, resultId):
                try:
                    upperList.append(Structure.objects.get(id=i))
                except:
                    break
        else:
            for i in range(resultId - 5, resultId):
                try:
                    upperList.append(Structure.objects.get(id=i))
                except:
                    break
        return render(request, 'dictionary/search.html', {'searchInput': searchInput, 'searchType': searchType, 'searchResult': searchResult, 'lowerList': lowerList, 'upperList': upperList, 'noResult': False})
        
        
def slugSearch(request, slug):
    searchResult = Structure.objects.get(slug=slug)
    resultId = searchResult.id
    lowerList = []
    upperList = []
    for i in range(resultId + 1, resultId + 6):
        try:
            lowerList.append(Structure.objects.get(id=i))
        except:
            break
    if resultId - 5 < 0:
        for i in range(1, resultId):
            try:
                upperList.append(Structure.objects.get(id=i))
            except:
                break
    else:
        for i in range(resultId - 5, resultId):
            try:
                upperList.append(Structure.objects.get(id=i))
            except:
                break
    return render(request, 'dictionary/search.html', {'searchInput': searchResult.turkish, 'searchResult': searchResult, 'lowerList': lowerList, 'upperList': upperList, 'noResult': False})