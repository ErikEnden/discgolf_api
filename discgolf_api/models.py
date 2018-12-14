from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=250)
    num_holes = models.PositiveSmallIntegerField()
    par = models.PositiveSmallIntegerField()
class Hole(models.Model):
    course_id = models.PositiveIntegerField()
    hole_num = models.PositiveSmallIntegerField()
    par = models.PositiveSmallIntegerField()
class Round(models.Model):
    course_id = models.PositiveIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
class Score(models.Model):
    round_id = models.PositiveIntegerField()
    hole_id = models.PositiveIntegerField()
    player_id = models.PositiveIntegerField()
    throw_count = models.PositiveIntegerField()