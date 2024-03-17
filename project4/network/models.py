from django.contrib.auth.models import AbstractUser
from django.db import models

# For debugging all default strings use all variables

class User(AbstractUser):
    # Min username length should be 4 but idk how to do that rn
    username = models.CharField(max_length=15)
    # Followers and Following handled in its own model
    
    def __str__(self):
        return f"User {self.id}: {self.username}"

class Post(models.Model):
    content = models.TextField()
    date = models.DateField()
    edited = models.BooleanField()
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="poster")
    
    def __str__(self):
        return f"{self.user}: {self.content} @ {self.date} | {self.edited}"
    
class Likes(models.Model):
    post = models.ForeignKey("Posts", on_delete=models.CASCADE, related_name="post")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user")
    
    def __str__(self):
        return f"{self.user} likes post -- {self.post}"    
    
class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="post")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user")
    
    def __str__(self):
        return f"{self.user}: {self.comment}"
    

# follower user points to following user (follower:foo, following:bar)
class Followerss(models.Model):
    follower = models.ForeignKey("User", on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey("User", on_delete=models.CASCADE, related_name="following")
    
    def __str__(self):
        return f"{self.follower} following {self.following}"
