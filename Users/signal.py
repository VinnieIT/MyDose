from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from MyDose.models import Medication_drugs,Medication

@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_profile(sender, instance, created, **kwargs):
   instance.profile.save()


# @receiver(post_save,sender=Medication)
# def save_date(sender,instance, created, **kwargs):
#         if created and instance.User_id:
#                 Medication_drugs.objects.update(date=instance.Med_date)



