"""Posts URLs"""

# Django
from django.urls import path
from django.contrib.auth.decorators import login_required

# Views
from posts import views


urlpatterns = [
    path(
        route='',
        view=login_required(views.PostFeedView.as_view()),
        name='feed'
    ),

    path(
        route='posts/new/',
        view=views.CreatePostView.as_view(),
        name='create_post'
    ),

    path(
        route='posts/<int:post_id>/',
        view=login_required(views.PostDetailView.as_view()),
        name='detail'
    ),
]
