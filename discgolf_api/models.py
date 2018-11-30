from django.db import models

# Create your models here.

class Course:
    num_holes = models.PositiveSmallIntegerField()
    par = models.PositiveSmallIntegerField()
class Hole:
    hole_num = models.PositiveSmallIntegerField()
    distance = models.PositiveSmallIntegerField()
class Round:
    course_id = models.PositiveIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
class Player:
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
class Score:
    round_id = models.PositiveIntegerField()
    hole_id = models.PositiveIntegerField()
    player_id = models.PositiveIntegerField()
    throw_count = models.PositiveIntegerField()