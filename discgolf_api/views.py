from django.shortcuts import render
from django.http import HttpResponse
from discgolf_api.serializers import CourseSerializer, HoleSerializer, RoundSerializer, PlayerSerializer, ScoreSerializer
from rest_framework.views import APIView
from rest_framework import generics
from .models import Course, Hole, Round, Player, Score


# Create your views here.

def index(request):
    return HttpResponse('here be discgolf')
class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseById(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class HoleList(generics.ListCreateAPIView):
    queryset = Hole.objects.all()
    serializer_class = HoleSerializer

class HoleById(generics.RetrieveUpdateAPIView):
    queryset = Hole.objects.all()
    serializer_class = HoleSerializer

class RoundList(generics.ListCreateAPIView):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer

class RoundById(generics.RetrieveUpdateAPIView):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer

class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerById(generics.RetrieveUpdateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class ScoreList(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class ScoreById(generics.RetrieveUpdateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer