from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers

from blog.models import Post


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "image", "body", "isMD")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def get_fields(self):
        fields = super().get_fields()
        for field in fields.values():
            field.read_only = True
        return fields


class GetPostSerializer(serializers.Serializer):
    slug = serializers.SlugField()


class EmptySerializer(serializers.Serializer):
    pass


class GetPostListSerializer(serializers.Serializer):
    username = serializers.SlugField()


class RatePostSerializer(serializers.Serializer):
    rating = serializers.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )
    post_slug = serializers.SlugField()