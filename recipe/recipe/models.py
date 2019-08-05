from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField("Bio", null=True, blank=True)
    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    time_req = models.CharField(max_length=20)
    instructions = models.TextField("Instructions", null=True, blank=True)
    def __str__(self):
        return self.title