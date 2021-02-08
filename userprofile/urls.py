from django.urls import path

from .views import votes, submissions

urlpatterns = [
    path('<str:username>/votes/', votes, name='votes'),
    path('<str:username>/submissions/', submissions, name='submissions'),
]
