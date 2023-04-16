from datetime import datetime
from django.db.models import F
from dictionary.models import Structure


def get_recent_searched_posts(limit=10):
    """
    Returns a list of the most recently searched posts.

    Args:
        limit (int): The maximum number of posts to return.

    Returns:
        list: A list of dictionaries, each representing a post and including its title and the number of times it was searched.
    """
    posts = Structure.objects.order_by('last_searched')[:limit]
    results = [{'title': post.title, 'search_count': post.search_count, 'slug': post.slug} for post in posts]

    # Update the search count and last searched time for the retrieved posts
    Structure.objects.filter(id__in=[post.id for post in posts]).update(
        search_count=F('search_count') + 1,
        last_searched=datetime.now()
    )

    return results