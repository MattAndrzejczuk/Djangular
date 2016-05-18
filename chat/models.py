from django.db import models
from polymorphic.models import PolymorphicModel
from django.contrib.auth.models import User
import json
from urllib.request import urlopen
from django.contrib.postgres.fields import JSONField
# Create your models here.
class JawnUser(models.Model):
    base_user = models.OneToOneField(User, related_name='jawn_user', )
    profile_pic = models.ImageField(upload_to="media/", blank=True, null=True)
    about_me = models.CharField(max_length=400, blank=True, null=True)
    follows = models.ManyToManyField('self', related_name='followers', symmetrical=False, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    SEX = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    sex = models.CharField(choices=SEX, null=True, blank=True, max_length=10)

    def __str__(self):
        return self.base_user.username


class Channel(models.Model):
    name = models.CharField(max_length=400, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(JawnUser, related_name='creator', blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    description = models.TextField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.name


class Message(PolymorphicModel):
    date_posted = models.DateTimeField(auto_now_add=True)
    jawn_user = models.ForeignKey(JawnUser, related_name='user', blank=True, null=True)
    channel = models.ForeignKey(Channel, related_name='messages')


class ImageMessage(Message):
    CHOICES = (('image', 'image'),)
    type = models.CharField(max_length=50, default='image', choices=CHOICES)
    image_url = models.ImageField(upload_to='media/')
    caption = models.TextField(max_length=1000, blank=True, null=True)


class TextMessage(Message):
    CHOICES = (('text', 'text'),)
    type = models.CharField(max_length=50, default='text', choices=CHOICES)
    text = models.TextField(max_length=1000)



class LinkMessage(Message):
    CHOICES = (('text', 'text'),)
    type = models.CharField(max_length=50, default='link', choices=CHOICES)
    text = models.TextField(max_length=1000)
    image_url = models.URLField(null=True, blank=True)
    headline = models.CharField(max_length=250)
    organization = models.CharField(max_length=250)

class RegionManager(models.Manager):
    def create_region(self, **kwargs):
        print(kwargs)
        kwargs['flickr_image'] = 'hellooooo'
        region = self.create(**kwargs)
        return region



class Region(models.Model):
    name = models.CharField(max_length=150)
    coordinates_long = models.FloatField()
    coordinates_lat = models.FloatField()
    flickr_image = models.CharField(max_length=150, null=True)
    google_json = JSONField()


    objects = RegionManager()

    def create(self, **kwargs):
        self.flickr_image = "IT WORKS!"# self.get_flickr_image(lat, long)
        self.save()
        print(kwargs)
        print(self.flickr_image)
        print(dir(self))


    # @classmethod
    # def save(self):
    #     # Run logic when a new object is created.
    #     self.flickr_image = "IT WORKS!"# self.get_flickr_image(lat, long)
    #     self.save()
    #     print(self)
    #     print(dir(self))
    #     return Super(Region, self).save(self)

    def get_flickr_image(self, lat, long):
        pass
        # Run logic for retreiving flickr img


class PrivateMessageRelationships(models.Model):
    channel = models.OneToOneField(Channel, related_name='channel', )
    user_recipient = models.ForeignKey(User, related_name='user_recipient', )
    user_sender = models.ForeignKey(User, related_name='user_sender', )
    channel_name = models.CharField(max_length=150) # may need to remove this later.
