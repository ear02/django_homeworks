from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200, null=False, unique=True)
    name = models.CharField(max_length=400, null=True)
    email = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return f'{self.username}'


class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    body = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.title}" by {self.user}'
