from django.db.models import Q
from dictionary.models import Structure

def searcher(query, structureType=None):
    if structureType == None:
        queryset = Structure.objects.filter(
            Q(turkish__icontains=query) |
            Q(english__icontains=query) |
            Q(english__icontains=query.lower()) |
            Q(turkish__icontains=query.lower())
        )
        
        return queryset
    else:
        queryset = Structure.objects.filter(
            Q(turkish__icontains=query) |
            Q(english__icontains=query) |
            Q(english__icontains=query.lower()) |
            Q(turkish__icontains=query.lower()),
            structureType = structureType
        )
        
        return queryset
