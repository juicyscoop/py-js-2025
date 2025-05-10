from django.db import models

band_choices = (
    (-1, "not defined"),
    (0, "rock"),
    (1, "metal"),
    (2, "pop"),
    (3, "hip-hop"),
    (4, "electronic"),
    (5, "reggae"),
    (6, "other")
)

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=64)
    year = models.IntegerField(null=True)
    still_active = models.BooleanField(default=True)
    genre = models.IntegerField(choices=band_choices, default=-1)

# Should contain all categories in Content Management System
class Category(models.Model):
    my_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)
    articles = models.ManyToManyField("Article")

article_choices = (
    (1, "in writing"),
    (2, "pending editor approval"),
    (3, "published"),
)
class Article(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True) # DATETIME DEFAULT CURRENT_TIMESTAMP()
    status = models.IntegerField(choices=article_choices)
    publish_date = models.DateField(null=True)
    removal_date = models.DateField(null=True)


rating_choices = (
    (0, "very bad"),
    (1, "poor"),
    (2, "average"),
    (3, "good"),
    (4, "very good"),
    (5, "excellent"),
)

class Album(models.Model):
    album_title = models.CharField(max_length=64)
    release_year = models.IntegerField()
    rating = models.IntegerField(choices=rating_choices)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, default=-1)

class Song(models.Model):
    title = models.CharField(max_length=128)
    duration = models.TimeField(null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default=-1)

class Person(models.Model):
    name = models.CharField(max_length=64)

class Position(models.Model):
    position_name = models.CharField(max_length=64)
    salary = models.FloatField()
    person = models.OneToOneField(Person, on_delete=models.CASCADE, default=-1)

