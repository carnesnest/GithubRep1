from django.db import models

class Post(models.Model):
  TopicID = models.IntegerField()
  PostName = models.CharField(max_length=255)
  TopicDescription = models.CharField(max_length=255)
  TopicPublishedDate = models.DateField()

class Comment(models.Model):
  TopicID = models.ForeignKey(Post,on_delete=models.CASCADE)
  CommentNumber = models.IntegerField()
  CommenterName = models.CharField(max_length=255)
  CommentText = models.CharField(max_length=255)
  
