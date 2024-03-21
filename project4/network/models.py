from django.contrib.auth.models import AbstractUser
from django.db import models

# For debugging all default strings use all variables

# Users inherit from AbstractUser, can have a username of min 4 char max 15
class User(AbstractUser):
    # Min username length should be 4 but idk how to do that rn
    username = models.CharField(max_length=15)
    following = models.ManyToManyField(
        'self',
        symmetrical = False,
        related_name = 'followers'
    )
    
# Posts contain content, date created, who created it, and if it has been edited or not
class Post(models.Model):
    # max len 280 to match twitter
    creater = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "author"
    )
    content = models.TextField(max_length = 280)
    date = models.DateField()
    edited = models.BooleanField(default = False)
    likes = models.ManyToManyField(
        User,
        related_name = "liked_posts"
    )
    
    def as_dict(self):
        return {
            "id": self.id,
            "creater": self.creater,
            "content": self.content,
            "date": self.date.strftime("%b %d %Y, %I:%M %p"),
            "edited": self.edited,
            "likes": self.likes.all()
        }
       
# Large Table of comments pointing to users and posts
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