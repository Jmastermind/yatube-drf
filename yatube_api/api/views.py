from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from api.mixins import CreateListViewSet
from api.permissions import AuthorOrReadOnly
from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)
from posts.models import Comment, Group, Post


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    @cached_property
    def _post(self) -> Post:
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def get_queryset(self):
        return self._post.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self._post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
