from blog.models import Post


def get_user_posts(username: str) -> list[Post]:
    return Post.objects.filter(user__username=username)
