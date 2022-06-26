from django.urls import path

from blog.views import HomeViews

urlpatterns = [
    path('', HomeViews.as_view(), name='post')
]
