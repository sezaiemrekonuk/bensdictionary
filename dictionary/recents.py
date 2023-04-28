from django.conf import settings
from datetime import datetime



from dictionary.models import Structure

def get_recent_searched_posts(limit=10):
    posts = Structure.objects.order_by('last_searched')[::-1]
    results = [{'title': post.turkish, 'search_count': post.search_count, 'slug': post.slug} for post in posts][:limit]
    return results
