from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from . import searcher, recents
from .models import Structure, Correct, typeOf


# Create your views here.

def index(request):
    return render(request, 'dictionary/index.html',
                  {'recent': recents.get_recent_searched_posts(5), 'allIdioms': Structure.objects.all(),
                   'idiomOfDay': Structure.objects.get(id=1), 'proverbOfDay': Structure.objects.get(id=2),
                   'itwds': Structure.objects.get(id=3)})


def search(request):
    if request.method == 'POST':
        searchInput = request.POST.get('search-input')
        searchType = request.POST.get('search-type')
        searchResult = None
        try:
            searchResult = searcher.searcher(searchInput, searchType)[0]
        except:
            return render(request, 'dictionary/search.html',
                          {'searchInput': searchInput, 'searchType': searchType, 'noResult': True})
        searchResult.last_searched = datetime.now()
        searchResult.search_count += 1
        searchResult.save()
        resultId = searchResult.id
        print('resultId:', resultId)
        lowerList = []
        upperList = []
        if searchType == 'Tüm Türler':
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
        else:
            structureLen = len(Structure.objects.all())
            listLen = 0
            iterator = resultId + 1
            while listLen < 5 and iterator < structureLen:
                try:
                    upperList.append(Structure.objects.get(id=iterator,
                                                           structureType=typeOf.objects.get(type=searchType)))
                    iterator += 1
                    listLen += 1
                except:
                    iterator += 1
            listLenTwo = 0
            iteratorTwo = resultId - 1
            while listLenTwo < 5 and iteratorTwo >= 0:
                try:
                    lowerList.append(Structure.objects.get(id=iteratorTwo,
                                                           structureType=typeOf.objects.get(type=searchType)))
                    iteratorTwo -= 1
                    listLenTwo += 1
                except:
                    iteratorTwo -= 1

        return render(request, 'dictionary/search.html',
                      {'searchInput': searchInput, 'searchType': searchType, 'searchResult': searchResult,
                       'lowerList': lowerList, 'upperList': upperList, 'noResult': False})


def slugSearch(request, slug):
    searchResult = Structure.objects.get(slug=slug)
    resultId = searchResult.id
    print(resultId)
    searchType = searchResult.structureType
    lowerList = []
    upperList = []

    if searchType == 'Tüm Türler':
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
    else:
        structureLen = len(Structure.objects.all())
        listLen = 0
        iterator = resultId + 1
        while listLen < 5 and iterator < structureLen:
            try:
                upperList.append(Structure.objects.get(id=iterator,
                                                       structureType=typeOf.objects.get(type=searchType)))
                iterator += 1
                listLen += 1
            except:
                iterator += 1
        listLenTwo = 0
        iteratorTwo = resultId - 1
        while listLenTwo < 5 and iteratorTwo >= 0:
            try:
                lowerList.append(Structure.objects.get(id=iteratorTwo,
                                                       structureType=typeOf.objects.get(type=searchType)))
                iteratorTwo -= 1
                listLenTwo += 1
            except:
                iteratorTwo -= 1

    return render(request, 'dictionary/search.html',
                  {'searchResult': searchResult,
                   'lowerList': lowerList, 'upperList': upperList, 'noResult': False})


def about(request):
    return render(request, 'dictionary/about.html')


def correct(request, slug):
    correctedStructure = get_object_or_404(Structure, slug=slug)
    if request.method == 'POST':
        if request.POST.get('iamhuman').lower() != 'ankara':
            return HttpResponse('You are not human! or??')
        corrector = request.POST.get('corrector')
        correction = request.POST.get('correction')
        corrector_mail = request.POST.get('corrector_mail')
        Correct.objects.create(corrector=corrector, correction=correction, toStructure=correctedStructure,
                               corrector_mail=corrector_mail)
        return HttpResponse('Thanks for your correction!')
    return redirect('slugSearch', slug=slug)
