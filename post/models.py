from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """
    Represents a blog post
    """
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    body = models.TextField()
    alt_text = models.CharField(max_length=100)
    published = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='my_photos')

    def __unicode__(self):
        return "Post #{}: {}".format(self.pk, self.title)


class Comment(models.Model):
    commenter = models.ForeignKey(User)
    text = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)
