from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model





class Post(models.Model):
    """
    A single Blog post
    """
    author = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)     
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images', default='images/crew--UP9VOibb64-unsplash.jpg')
    category = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=255, null=True)
    
    
    def __str__(self):
        return self.title

        
class Comment(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)     
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    attending = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text