from django.db import models

# Create your models here.
class BeerApp(models.Model):
    beerid = models.AutoField(primary_key=True)
    comments = models.CharField(max_length=2000)
    beername = models.CharField(max_length = 45)
    style = models.CharField(max_length=45)
    ABV = models.CharField(max_length=45)
    beer_img_name = models.CharField(max_length=45)

    class Meta:
        db_table ="beers"