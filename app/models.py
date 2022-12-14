from django.db import models

# Create your models here.

# admin.site.register(Table Name)
class User(models.Model):
    # note: charfield has max length 255 chars
    # TextField allows for longer entries
    # null/blank: we can't submit a form with no values
    handle = models.CharField(max_length=28)
    password = models.CharField(max_length=255)
    email = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self) -> str:
        return self.handle

class Upload(models.Model):
    title = models.CharField(max_length=64, null=False)
    content = models.TextField(null=False)
    # auto_now can change
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    latitude = models.FloatField(default=48.2625728)
    longitude = models.FloatField(default=11.6677239)

    def __str__(self) -> str:
        return self.title

class Link(models.Model):
    postId = models.IntegerField(null=False)
    url = models.TextField()

    def __str__(self) -> str:
        return self.url