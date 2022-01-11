from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from blog import serializers
from blog.serializers import PostSerializer
from blog.services.create_new_post import create_new_post
from blog.services.get_post_by_slug import get_post_by_slug
from blog.services.get_top_posts import get_top_posts
from blog.services.get_user_posts import get_user_posts
from blog.services.rate_post import rate_post


def _serialise_post_list(posts: list):
    data = {}
    for post in posts:
        data[post.id] = PostSerializer(post).data
    return data


class PostSet(viewsets.GenericViewSet):
    permission_classes = [
        AllowAny,
    ]
    serializer_class = serializers.EmptySerializer
    serializer_classes = {
        "post_create": serializers.PostCreateSerializer,
        "post": serializers.GetPostSerializer,
        "user_post_list": serializers.GetPostListSerializer,
        "rate_post": serializers.RatePostSerializer
    }

    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()

    @action(
        methods=[
            "POST",
        ],
        detail=False,
    )
    def user_post_list(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        posts = get_user_posts(serializer.data["username"])

        return Response(data=_serialise_post_list(posts), status=status.HTTP_200_OK)

    @action(
        methods=[
            "GET",
        ],
        detail=False,
    )
    def top_posts(self, request):
        posts = get_top_posts()
        return Response(data=_serialise_post_list(posts), status=status.HTTP_200_OK)

    @action(
        methods=[
            "POST",
        ],
        detail=False,
        permission_classes=[
            IsAuthenticated,
        ],
    )
    def post_create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = create_new_post(user_id=request.user.id, **serializer.data)
        data = PostSerializer(post).data
        print(data)
        return Response(data=data, status=status.HTTP_201_CREATED)

    @action(
        methods=[
            "POST",
        ],
        detail=False,
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = get_post_by_slug(serializer.data["slug"])
        data = PostSerializer(post).data
        return Response(data=data, status=status.HTTP_200_OK)

    @action(
        methods=[
            "POST",
        ],
        detail=False,
        permission_classes=[
            IsAuthenticated,
        ],
    )
    def rate_post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rate = rate_post(request.user, serializer.data["post_slug"], serializer.data["rating"])
        return Response(data={"message": f"{rate.rating} - {rate.post.rating}"}, status=status.HTTP_201_CREATED)
