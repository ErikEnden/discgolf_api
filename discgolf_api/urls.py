from django.urls import path
from .views import *

from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('courses/', CourseList.as_view(), name='CourseList'),
    path('courses/<int:pk>', CourseById.as_view(), name='CourseListById'),
    path('holes/', HoleList.as_view(), name='HoleList'),
    path('holes/<int:pk>', HoleById.as_view(), name='HoleList'),
    path('rounds/', RoundList.as_view(), name='RoundList'),
    path('rounds/<int:pk>', RoundById.as_view(), name='RoundList'),
    path('players/', PlayerList.as_view(), name='PlayerList'),
    path('players/<int:pk>', PlayerById.as_view(), name='PlayerListById'),
    path('scores/', ScoreList.as_view(), name='ScoreList'),
    path('scores/<int:pk>', ScoreById.as_view(), name='ScoreListById')
]