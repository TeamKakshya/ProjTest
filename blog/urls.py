from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from .views import post_list,post_detail,upvote_post,gallery,EventCreateView,event_list,participate
from .views import EventDeleteView,EventUpdateView

    # taking some function based views
urlpatterns=[
    path('',post_list,name='blog-home'),
    path('user/<str:username>/',UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/',post_detail,name='post-detail'),
    path('post/upvote/',upvote_post,name='upvote_post'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('event/new/',EventCreateView.as_view(),name='event-create'),
    path('event/<int:pk>/update/',EventUpdateView.as_view(),name='event-update'),
    path('event/list/',event_list,name='event-list'),
    path('event/<int:pk>/delete/',EventDeleteView.as_view(),name='event-delete'),
    path('event/participate/',participate,name="participate"),
    path('about/',views.about,name='blog-about'),
    path('gallery/',gallery,name="gallery"),

]
