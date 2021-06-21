from django.urls import path
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePost,DeletepostView
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('NewPost/',AddPostView.as_view(),name="addpost"),
    path('article/edit/<int:pk>',UpdatePost.as_view(),name="updatepost"),
    path('article/<int:pk>/remove',DeletepostView.as_view(),name="deletepost"),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article'),
]