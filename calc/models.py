from django.db import models
from datetime import datetime
from django.utils import timezone



# Create your models here.
class First(models.Model):
    event = models.CharField(max_length=200, default='Type the event here')
    image1 = models.ImageField(upload_to='pic', blank=True)
    image2 = models.ImageField(upload_to='pic', blank=True)
    image3 = models.ImageField(upload_to='pic', blank=True)
    city = models.CharField(max_length=200, default='Chennai/Solapur')
    pub_date = models.DateTimeField('date_published', default=datetime.now())
    video_url = models.URLField(default=1)



    class Meta:
        verbose_name_plural='Firsts'

    def __str__(self):
        return self.event