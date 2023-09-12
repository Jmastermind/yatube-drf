from django.urls import include, path
from rest_framework import routers

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = '%(app_label)s'

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
router.register('follow', FollowViewSet, basename='follow')
router.register('groups', GroupViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
