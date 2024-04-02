from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32)
    date_joined = models.DateTimeField(auto_now_add=True)
    # posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='user')
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

