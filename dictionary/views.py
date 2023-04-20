
from django.shortcuts import render
from .models import Structure
from . import searcher, recents
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'dictionary/index.html', {'recent': recents.get_recent_searched_posts(5), 'allIdioms': Structure.objects.all(), 'idiomOfDay': Structure.objects.get(id=1), 'proverbOfDay': Structure.objects.get(id=2)})

def search(request):
    if request.method == 'POST':
        searchInput = request.POST.get('search-input')
        searchType = request.POST.get('search-type')
        searchResult = None
        try:
            searchResult = searcher.searcher(searchInput, searchType)[0]
        except:
            return render(request, 'dictionary/search.html', {'searchInput': searchInput, 'searchType': searchType, 'noResult': True})
        searchResult.last_searched = datetime.now()
        searchResult.search_count += 1
        searchResult.save()
        resultId = searchResult.id
        lowerList = []
        upperList = []
        for i in range(resultId + 1, resultId + 6):
            try:
                lowerList.append(Structure.objects.get(id=i))
            except:
                break
        if resultId - 5 <= 0:
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
    # else:
    #     searchInput = request.POST.get('search-input')
    #     searchType = request.POST.get('search-type')
    #     searchResult = request.session.get('SEARCHRESULT')
    #     searchResult.last_searched = datetime.now()
    #     searchResult.search_count += 1
    #     searchResult.save()
    #     resultId = searchResult.id
    #     lowerList = []
    #     upperList = []
    #     for i in range(resultId + 1, resultId + 6):
    #         try:
    #             lowerList.append(Structure.objects.get(id=i))
    #         except:
    #             break
    #     if resultId - 5 < 0:
    #         for i in range(1, resultId):
    #             try:
    #                 upperList.append(Structure.objects.get(id=i))
    #             except:
    #                 break
    #     else:
    #         for i in range(resultId - 5, resultId):
    #             try:
    #                 upperList.append(Structure.objects.get(id=i))
    #             except:
    #                 break
    #     return render(request, 'dictionary/search.html', {'searchInput': searchInput, 'searchType': searchType, 'searchResult': searchResult, 'lowerList': lowerList, 'upperList': upperList, 'noResult': False})
        
        
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
    if resultId - 5 <= 0:
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

def about(request):
    return render(request, 'dictionary/about.html')