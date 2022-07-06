from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Media(models.Model):
    """this handles the data about what type of material was used to create the art work"""
    media = models.CharField(null=False)

    def __str__(self):
        return self.media


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
    media = models.ForeignKey(
        Media, on_delete=models.CASCADE, related_name="media")
    is_framed = models.BooleanField(default=False, null=False)
    handling_tips = models.TextField()

    class Meta:
        """ this oders the post from oldest to news comments"""
        ordering: ['date_completed']

    def __str__(self):
        return self.title


class Comment(models.Model):
    """handles the data for the comments users make"""
    art = models.ForeignKey(
        Art, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=False)
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=False)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """oders the comments from newsest to oldest"""
        ordering = ['created_on']

    def __str__(self):
        return f"Comment: {self.body} by {self.name}"


class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
