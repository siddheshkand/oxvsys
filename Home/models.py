from django.db import models
from taggit.managers import TaggableManager


class ProjectDetail(models.Model):
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=250)
    thumbnail = models.ImageField()
    description = models.TextField()
    icon = models.ImageField()
    period_start = models.DateTimeField()
    period_end = models.DateTimeField()
    tag = TaggableManager()
    position = models.IntegerField(default=0)

    # https://djangosnippets.org/snippets/10638/
    # ^ to solve upload problem
    def __str__(self):
        return self.title + self.sub_title


class CustomerDetail(models.Model):
    email = models.EmailField()
    contact_nos = models.PositiveIntegerField()
    message = models.TextField()
    requirements = models.TextField()


