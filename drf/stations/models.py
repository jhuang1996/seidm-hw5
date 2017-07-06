from django.db import models

# Create your models here.
#class Station(models.Model):
#    rpk = models.AutoField(primary_key=True)
#    name = models.CharField(max_length=10, null=False)
#    sid = models.CharField(max_length=5, null=False)
#    timestamp = models.DateTimeField(null=False)
#    r_10m = models.DecimalField(max_digits=6, decimal_places=1)
#    r_1h = models.DecimalField(max_digits=6, decimal_places=1)
#    r_3h = models.DecimalField(max_digits=6, decimal_places=1)
#    r_6h = models.DecimalField(max_digits=6, decimal_places=1)
#    r_12h = models.DecimalField(max_digits=6, decimal_places=1)
#    r_24h = models.DecimalField(max_digits=6, decimal_places=1)
#    r_td = models.DecimalField(max_digits=6, decimal_places=1)
#    r_yd = models.DecimalField(max_digits=6, decimal_places=1)
#    r_2d = models.DecimalField(max_digits=6, decimal_places=1)

class A136(models.Model):
    rpk = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    sid = models.CharField(max_length=5)
    timestamp = models.CharField(max_length=25)
    r_10m = models.FloatField(blank=True, null=True)
    r_1h = models.FloatField(blank=True, null=True)
    r_3h = models.FloatField(blank=True, null=True)
    r_6h = models.FloatField(blank=True, null=True)
    r_12h = models.FloatField(blank=True, null=True)
    r_24h = models.FloatField(blank=True, null=True)
    r_td = models.FloatField(blank=True, null=True)
    r_yd = models.FloatField(blank=True, null=True)
    r_2d = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'a136'
