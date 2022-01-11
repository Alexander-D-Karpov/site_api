from blog.models import UserRate
from blog.services.get_post_by_slug import get_post_by_slug
from common.error import ValidatorException
from users.models import Person


def rate_post(
        user: Person,
        post_slug: str,
        rating: int
) -> UserRate:
    if not 1 <= rating <= 5:
        raise ValidatorException("provided rating is incorrect", "RateEr", 467)

    post = get_post_by_slug(post_slug)
    if UserRate.objects.filter(user=user, post__slug=post_slug).exists():
        rate_count = UserRate.objects.get(user=user, post__slug=post_slug).rating
        post.rating = (post.rating * post.rating_count - rate_count + rating) / post.rating_count
        post.save(update_fields=["rating"])

        rate = UserRate.objects.get(user_id=user.id, post_id=post.id)
        rate.rating = rating
        rate.save(update_fields=["rating"])
        return rate

    post.rating = (post.rating * post.rating_count + rating) / (post.rating_count + 1)
    post.rating_count += 1
    post.save(update_fields=["rating_count", "rating"])

    user_rate = UserRate.objects.create(user_id=user.id, post_id=post.id, rating=rating)
    user_rate.save()
    return user_rate
