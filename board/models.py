from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length=120)
    post_pub_date = models.DateTimeField('publish date')
    post_desc = models.TextField()
    post_author = models.CharField(max_length=24)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_author = models.CharField(max_length=24)