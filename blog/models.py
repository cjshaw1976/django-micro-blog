from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import datetime

LIKE_CHOICES = (
    ("LIKE", "Like"),
    ("DISLIKE", "Dislike"),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userProfile')
    secret_word = models.CharField(max_length=32)
    email_confirmed = models.BooleanField(default=False)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField('profile picture',
                               upload_to='static/media/images/avatars/',
                               null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userProfile.save()


class Followers(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'follower',)

class Blogs(models.Model):
    user = models.ForeignKey(User, related_name='blog', on_delete=models.CASCADE)
    created = models.DateTimeField(default=datetime.now, blank=True)
    heading = models.TextField(max_length=32)
    text = models.TextField(max_length=256)
    attachment = models.FileField(upload_to='static/media/blog/attachments/',
                                  null=True, blank=True)

    class Meta:
        unique_together = ('user', 'heading')


class Likes(models.Model):
    user = models.ForeignKey(User, related_name="like")
    blog = models.ForeignKey('Blogs', on_delete=models.CASCADE)
    like = models.CharField(max_length=7, choices=LIKE_CHOICES, default="Like")

    class Meta:
        unique_together = ('user', 'blog')
