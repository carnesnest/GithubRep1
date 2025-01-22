from django.urls import path
from . import views  # Import the views module from the paper app

urlpatterns = [
    path('main/', views.main, name='main'),
    path('mypost/', views.post_list, name='mypost'),  # URL: /mypost/
    path('post/', views.post_list, name='post'),      # URL: /post/
    path('mycomment/', views.comment_list, name='mycomment'),  # URL: /mycomments/
    path('comment/<int:id>/', views.comment_list, name='comment'),      # URL: /comments/
]