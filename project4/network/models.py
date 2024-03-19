from django.contrib.auth.models import AbstractUser
from django.db import models

# For debugging all default strings use all variables

# Users inherit from AbstractUser, can have a username of min 4 char max 15
class User(AbstractUser):
    # Min username length should be 4 but idk how to do that rn
    username = models.CharField(max_length=15)
    
    def __str__(self):
        return f"User {self.id}: {self.username}"

# Posts contain content, date created, who created it, and if it has been edited or not
class Post(models.Model):
    # max len 280 to match twitter
    content = models.TextField(max_length=280)
    date = models.DateField()
    edited = models.BooleanField(default=False)
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="poster")
    
    def __str__(self):
        return f"{self.user}: {self.content} @ {self.date} | {self.edited}"
    
# Which user likes which post
class Likes(models.Model):
    post = models.ForeignKey("Posts", on_delete=models.CASCADE, related_name="post")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user")
    
    def __str__(self):
        return f"{self.user} likes post -- {self.post}" 
       
# Large Table of comments pointing to users and posts
class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="post")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user")
    
    def __str__(self):
        return f"{self.user}: {self.comment}"
    

# follower user points to following user (follower:foo, following:bar)
class Followers(models.Model):
    follower = models.ForeignKey("User", on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey("User", on_delete=models.CASCADE, related_name="following")
    
    def __str__(self):
        return f"{self.follower} following {self.following}"
