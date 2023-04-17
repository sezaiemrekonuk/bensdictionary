from datetime import datetime
from django.db.models import F
from dictionary.models import Structure


def get_recent_searched_posts(limit=10):
    posts = Structure.objects.order_by('last_searched')[:limit]
    results = [{'title': post.english, 'search_count': post.search_count, 'slug': post.slug} for post in posts][::-1]

    # Update the search count and last searched time for the retrieved posts
    Structure.objects.filter(id__in=[post.id for post in posts]).update(
        search_count=F('search_count') + 1,
        last_searched=datetime.now()
    )

    return results