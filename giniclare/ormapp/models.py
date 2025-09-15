from django.db import models
from django.contrib import admin
class Car(models.Model):
    car_id=models.IntegerField(primary_key=True)
    brand=models.CharField(max_length=20)
    car_model=models.CharField(max_length=20)
    email=models.EmailField()
    dop=models.DateField()
class CarAdmin(admin.ModelAdmin):
    list_display=['car_id','brand','car_model','email','dop']
# Create your models here.
