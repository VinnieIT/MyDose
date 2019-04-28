from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Medication(models.Model): 
    User_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Med_date = models.DateTimeField(auto_now_add= True)
    diagnosis = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.diagnosis

class Medication_drugs(models.Model):
    med_id = models.ForeignKey(Medication, on_delete=models.CASCADE)
    drug_name = models.CharField(max_length = 250)
    frequency = models.IntegerField()
    mode_of_administration = models.CharField(max_length = 100)
    date =models.DateTimeField(auto_now=True)
    duration = models.IntegerField()
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.drug_name 

    def get_absolute_url(self):
        return reverse("profile")
    
class time_period(models.Model):
    id = models.AutoField(max_length = 10, primary_key=True)
    time_name = models.CharField(max_length = 50)
    start_time= models.TimeField()
    end_time= models.TimeField()

class drug_period(models.Model):
    id = models.IntegerField(primary_key = True)
    med_drug_id = models.ForeignKey(Medication_drugs, on_delete= models.CASCADE)
    time_period_id = models.ForeignKey(time_period, on_delete= models.CASCADE)

class Reminder(models.Model):
     from_diagnosis = models.ForeignKey(Medication,on_delete =models.PROTECT)
     from_med_drugs = models.ForeignKey(Medication_drugs,on_delete =models.PROTECT)
     reminder_time_morning= models.TimeField()
     reminder_time_midday= models.TimeField()
     reminder_time_evening= models.TimeField()



    

