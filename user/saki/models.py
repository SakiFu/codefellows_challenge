import datetime
from django.db import models
from django.utils import timezone
from datetime import datetime
from time import time


def get_upload_file_name(instance, filename):
    return "uploaded_files/%s" % (filename)

class User(models.Model):
    class Meta:
        verbose_name_plural = "Users"
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, default='None')
    email = models.EmailField(max_length=30, default='None')
    thumbnail = models.FileField(upload_to=get_upload_file_name, default = 'None')

    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.first_name
        return self.last_name
        return self.email
        return self.thumbnail
        
    def admin_image(self):
        return '<img src="%s"/>' % self.thumbnail
    admin_image.allow_tags = True


    
