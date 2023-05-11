from django.db import models

# Create your models here.
class contactTable(models.Model):
    s_no = models.AutoField()
    nameC = models.CharField(max_length=256)
    phoneC = models.CharField( max_length=50)
    emailC = models.EmailField( max_length=254)
    choice = models.CharField( max_length=50)