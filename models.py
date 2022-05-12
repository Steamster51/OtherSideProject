from pyexpat import model
from django.db import models
from django.forms import Textarea
from matplotlib import widgets

# Create your models here.
class contactmsg(models.Model):
    dbfullName = models.CharField(max_length=50)
    dbemail = models.CharField(max_length=50)
    dbmessage = models.TextField()
    def __str__(self):
        return self.dbfullName + " " + self.dbemail
