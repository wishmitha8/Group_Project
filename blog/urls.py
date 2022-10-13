from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    FollowsListView,
    FollowersListView,
    postpreference,
    post_list)
from .import views
from django.urls import include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/',views.about, name='blog-about'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
       path('api/posts', post_list)
]
