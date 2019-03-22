from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Medication(models.Model): 
    id = models.IntegerField(primary_key=True,max_length=100)
    User_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Med_date = models.DateField(auto_now_add= True)
    diagnosis = models.CharField(max_length=250)
    is_active = models.CharField(max_length=10,)

class Medication_drugs(models.Model):
    id = models.AutoField(max_length=250,primary_key= True)
    med_id = models.ForeignKey(Medication, on_delete=models.CASCADE)
    drug_name = models.CharField(max_length = 250)
    frequency = models.IntegerField()
    mode_of_administration = models.CharField(max_length = 100)
    duration = models.IntegerField()
    quantity = models.IntegerField()

class time_period(models.Model):
    id = models.AutoField(max_length = 10, primary_key=True)
    time_name = models.CharField(max_length = 50)
    start_time= models.TimeField()
    end_time= models.TimeField()

class drug_period(models.Model):
    id = models.IntegerField(primary_key = True)
    med_drug_id = models.ForeignKey(Medication_drugs, on_delete= models.CASCADE)
    time_period_id = models.ForeignKey(time_period, on_delete= models.CASCADE)



    

