from django.db.models import F
from django.shortcuts import get_object_or_404

from blog.models import Post
from common.error import ValidatorException


def get_post_by_slug(slug: str) -> Post:
    """returns post instance or 404 on slug"""
    post = get_object_or_404(Post, slug=slug)
    post.post_views += 1
    post.save(update_fields=["post_views"])
    return post
