from django.utils.text import slugify

from blog.models import Post


def create_new_post(
        title: str,
        user_id: int,
        **extra_fields
) -> Post:
    slug = slugify(title)
    create = Post.objects.create(title=title, user_id=user_id, slug=slug, **extra_fields)
    post = create
    post.save()
    return post
