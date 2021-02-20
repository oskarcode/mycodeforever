from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django_resized import ResizedImageField



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    header_image = ResizedImageField(size=[500, 300], crop=['middle', 'center'],quality=100,upload_to= 'images/', blank=True, null=True)
    #header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    date_posted = models.DateField(default = timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})
