from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )
    
    def __str__(self):
        return self.username


class Post(models.Model):
    creater = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="author"
    )
    content = models.TextField(max_length=280)
    date = models.DateField()
    edited = models.BooleanField(default=False)
    id = models.IntegerField(primary_key=True)
    likes = models.ManyToManyField(
        User,
        related_name="liked_posts",
        blank=True
    )
       

class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name="comments"
    )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
    )