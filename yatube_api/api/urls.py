from rest_framework.authtoken import views
from rest_framework import routers

from django.urls import include, path

from .views import CommentViewSet, GroupViewSet, PostViewSet


router = routers.DefaultRouter()
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router.register('groups', GroupViewSet, basename='group' )
router.register('posts', PostViewSet, basename='post')


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]