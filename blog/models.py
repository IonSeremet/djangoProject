from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    category = models.CharField(max_length=255, default='uncategorized')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)