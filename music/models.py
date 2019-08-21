from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=250, blank=True)
	birth_date = models.DateField(null=True, blank=True)


# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		Profile.objects.create(user=instance)
# 	instance.profile.save()


class Category(models.Model):
	category_title = models.CharField(max_length=250)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.category_title


class Album(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	album_title = models.CharField(max_length=500)
	artist = models.CharField(max_length=250)
	genre = models.CharField(max_length=100)
	album_logo = models.FileField()
	is_favorite = models.BooleanField(default=False)
	created_at = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return self.album_title + ' - ' + self.artist


class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	song_title = models.CharField(max_length=250)
	audio_file = models.FileField(default='')
	is_favorite = models.BooleanField(default=False)
	created_at = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return self.song_title
















