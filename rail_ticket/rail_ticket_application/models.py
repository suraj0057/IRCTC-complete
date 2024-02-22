from django.db import models

# Create your models here.

class Train(models.Model):
       trainNo=models.BigIntegerField()
       trainName=models.CharField(max_length=100)
       source=models.CharField(max_length=100)
       destination=models.CharField(max_length=100)
       journeyDate=models.DateField(default="2022-12-02")
       arrivalTime=models.TimeField(default='00:00:00') 
       departureTime=models.TimeField(default='00:00:00') 
       sleeperAvailable=models.BigIntegerField(default=0)
       sleeperWaiting=models.BigIntegerField(default=0)
       acAvailable=models.BigIntegerField(default=0)
       acWaiting=models.BigIntegerField(default=0)
       sleeperPrice=models.BigIntegerField(default=0)
       acPrice=models.BigIntegerField(default=0)
       

class Ticket_details(models.Model):
       ticket_id=models.BigIntegerField()
       trainNumName= models.CharField(max_length=150,default="")
       journey_date=models.DateField(default="2022-12-02")
       fromStn=models.CharField(max_length=100,default="")
       destStn=models.CharField(max_length=100, default="")
       seating_class=models.CharField(max_length=10,default="")
       pDetails=models.JSONField(default="")
       
       
