from django.db import models
from django.utils import timezone


class BucketList(models.Model):
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=timezone.now())
    date_modified = models.DateTimeField(default=timezone.now())
    created_by = models.ForeignKey('auth.User')

    def __init__(self, name, created_by):
        self.title = name
        self.created_by = created_by

    def __str__(self):
        # Use the object title to represent the object
        return self.title

    def save(self):
        self.save()


class Items(models.Model):
    Bucket = models.ForeignKey(BucketList)
    title = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=timezone.now())
    date_modified = models.DateTimeField(default=timezone.now())

    def __init__(self, name):
        self.title = name

    def __str__(self):
        return self.title

    def save(self):
        self.save()
