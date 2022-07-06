from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Art(models.Model):
    """this handles the data for the art works and its details"""
    title = models.CharField(null=False)
    caption = models.TextField()
    date_completed = models.DateField(auto_now=False)
    price = models.IntegerField()
    art_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(User, related_name='art_likes', blank=True)
    size = models.CharField(max_length=100, unique=False, default='cm')
    is_available = models.BooleanField(default=False, null=False)
    media = models.ForeignKey(Media, on_delete=models.CASCADE, related_name="media")
    is_framed = models.BooleanField(default=False, null=False)
    handling_tips = models.TextField()

    class Meta:
        """ this oders the post from oldest to news comments"""
        ordering: ['-completed_on']
