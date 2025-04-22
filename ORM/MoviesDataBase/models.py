from django.db import models
from django.contrib import admin
class Movie(models.Model):
	Movie_name=models.CharField(max_length=50)
	Ratings=models.FloatField(primary_key="Ratings")
	Cast=models.CharField(max_length=50)
	Release_year=models.DateField()
	Genre=models.CharField(max_length=50)
class MovieAdmin(admin.ModelAdmin):
	list_display=('Movie_name','Ratings','Cast','Release_year','Genre')