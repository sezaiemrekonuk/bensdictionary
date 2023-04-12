from django.db.models import Q
from dictionary.models import Structure

def searcher(query, structureType):
    queryset = Structure.objects.filter(
        Q(turkish__icontains=query) |
        Q(english__icontains=query) |
        Q(english__icontains=query.lower()) |
        Q(turkish__icontains=query.lower()),
        structureType = structureType
    )
    return queryset

def searcher(query):
    queryset = Structure.objects.filter(
        Q(turkish__icontains=query) |
        Q(english__icontains=query) |
        Q(english__icontains=query.lower()) |
        Q(turkish__icontains=query.lower())
    )
    return queryset