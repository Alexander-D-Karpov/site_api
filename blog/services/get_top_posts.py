from blog.models import Post


def get_top_posts() -> list[Post]:
    posts = sorted(Post.objects.all(), key=lambda x: x.post_views, reverse=True)
    return posts
