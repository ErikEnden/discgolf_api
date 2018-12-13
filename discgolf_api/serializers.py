from .models import Course, Hole, Round, Player, Score
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'name',
            'num_holes',
            'par'
        ]
class HoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hole
        fields = [
            'id',
            'hole_num',
            'distance'
        ]
class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = [
            'id',
            'course_id',
            'start_time',
            'end_time'            
        ]
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'password'
        ]
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = [
            'id',
            'round_id',
            'hole_id',
            'player_id',
            'throw_count'
        ]