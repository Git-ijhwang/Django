from django.db import models
from django.urls import reverse

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    target_url = models.URLField('Site_URL')

    def __str__(self):
        return "Name: "+self.site_name+", Address: "+self.target_url

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])