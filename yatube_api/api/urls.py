from rest_framework import routers
from rest_framework.authtoken import views
from django.contrib import admin
from django.urls import include, path

from api.views import GroupViewSet, PostViewSet, CommentViewSet



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