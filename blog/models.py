from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import Person as User


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    image = models.ImageField(upload_to="", blank=True)
    slug = models.SlugField(max_length=150, blank=False, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    post_views = models.IntegerField(default=0)
    isMD = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Rating
    rating = models.FloatField(
        default=0, validators=[MaxValueValidator(5), MinValueValidator(0)]
    )
    rating_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserRate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(
        blank=False, validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    def __str__(self):
        return self.user.username + " " + self.post.title + " " + str(self.rating)


class Comment(models.Model):
    name = models.CharField(max_length=100, blank=True)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)
