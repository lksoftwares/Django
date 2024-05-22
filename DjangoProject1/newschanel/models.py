from django.db import models
from tinymce.models import HTMLField
class NewsChanel(models.Model):
    newsTitle=models.CharField(max_length=50)
    newsInfo=HTMLField()
    newsImage=models.FileField(upload_to="news/",max_length=255,null=True,default=None)
# Create your models here.
