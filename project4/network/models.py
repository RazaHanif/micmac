from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers'
    )

    
class Post(models.Model):
    creater = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="author"
    )
    content = models.TextField(max_length=280)
    date = models.DateField()
    edited = models.BooleanField(default=False)
    likes = models.ManyToManyField(
        User,
        related_name="liked_posts"
    )
    
    def as_dict(self):
        return {
            "id": self.id,
            "creater": self.creater,
            "content": self.content,
            "date": self.date.strftime("%b %d %Y, %I:%M %p"),
            "edited": self.edited,
            "likes": self.likes.count()
        }
       

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