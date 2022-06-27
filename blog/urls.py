from django.urls import path

from blog.views import HomeViews, PostView, CategoryViews, get_post

urlpatterns = [
    path('', HomeViews.as_view(), name='home'),
    path('category/<str:slug>', CategoryViews.as_view(), name='category'),
    # path('post/<str:slug>', get_post, name='post'),

    # path('<int:post_id>', DetailsView.as_view(), name='post'),

    # path('post/<int:post_id>/', DetailsView.as_view(), name='post'),
    path('post/<str:slug>/', PostView.as_view(), name='post'),
]
