from django.db.models import Q
from dictionary.models import Structure, typeOf

def searcher(query, structureType):
    if structureType == 'Tüm Türler':
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
            structureType = typeOf.objects.get(type=structureType)
        )
        return queryset
