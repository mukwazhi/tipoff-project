from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Information(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(blank=True, upload_to="information/images/")
    color_code = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Brand(models.Model):
    logo = models.ImageField(upload_to='logos/images/')
    banner = models.ImageField(upload_to='brand/images/')
    mkting = models.ImageField(upload_to="mkting/image/", blank=True)


class Article(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=3000)
    created_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
