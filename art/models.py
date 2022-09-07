from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Media(models.Model):
    """
    Creates the type of media used for the art work
    """
    type = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        ordering: ['type']

    def __str__(self):
        return self.type


class Category(models.Model):
    """
    Creates catagories for art works
    """
    type = models.CharField(max_length=25, null=False, blank=False)

    class Meta:
        ordering: ['type']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.type


class Art(models.Model):
    """
    this handles the data for the art works and its details
    """
    title = models.CharField(max_length=250, null=False)
    caption = models.TextField()
    date_completed = models.DateField(auto_now=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    art_image = CloudinaryField('image', blank=False)
    likes = models.ManyToManyField(User, related_name='art_likes', blank=True)
    size = models.CharField(max_length=100, unique=False, default='cm')
    is_available = models.BooleanField(default=False, null=False)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_framed = models.BooleanField(default=False, null=False)
    handling_tips = models.TextField()

    class Meta:
        """ this oders the post from oldest to news comments"""
        ordering: ['date_completed']

    def __str__(self):
        return self.title
    
    def total_number_of_likes(self):
        """this counts the total number of likes"""
        return self.likes.count()


class Comment(models.Model):
    """handles the data for the comments users make"""
    art = models.ForeignKey(
        Art, on_delete=models.CASCADE, related_name="art_commented_on")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=False)
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True,
        blank=False, related_name="commenting_user_name")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """oders the comments from newsest to oldest"""
        ordering = ['created_on']

    def __str__(self):
        return f"Comment: {self.body} by {self.name}"


class Newsletter(models.Model):
    """collects data for users who joined the mail list"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=False)
    join = models.BooleanField(default=False, null=False)
    joined_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """oders the users on the date they joined"""
        ordering = ['joined_on']

    def __str__(self):
        return f"{self.user.username}"
