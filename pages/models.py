# projects/models.py

from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills = models.ManyToManyField(Skill)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
