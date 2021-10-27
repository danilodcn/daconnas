import datetime

from django.db import models


class Post(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True, null=False, blank=False)
    title = models.CharField(max_length=60, null=False, blank=False)
    description = models.TextField(default="", blank=False, null=True)
    content = models.TextField(default="", blank=False, null=True)
    create_at = models.DateTimeField(auto_now=True, blank=False, null=False)


class User(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True, null=False, blank=False)
    name = models.CharField(max_length=60, null=False, blank=False)
    login = models.CharField(max_length=50, null=False, blank=False, unique=True)
    email = models.EmailField(null=False, unique=True)
    image = models.ImageField(null=False)
    author = models.BooleanField(default=False, blank=False, null=False)

    # posts = models.ManyToManyField(Post, through="Publication")


class Speaker(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True, null=False, blank=False)
    name = models.CharField(max_length=60, null=False, blank=False)
    image = models.ImageField(blank=False)
    description = models.TextField(max_length=200, default="", blank=False, null=True)
    content = models.TextField(default="", blank=False, null=True)
    published = models.BooleanField(default=False, blank=False, null=False)

    # posts = models.ManyToManyField(Post, through="Publication")


class Topic(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True, null=False, blank=False)
    name = models.CharField(max_length=60, null=False, blank=False)

    # posts = models.ManyToManyField(Post, through="Publication")


class Publication(models.Model):
    # id = models.IntegerField(primary_key=True, auto_created=True, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    visualizations = models.IntegerField(blank=False, null=False, default=0)
    published_at = models.DateTimeField(auto_now=True, blank=False, null=False)
