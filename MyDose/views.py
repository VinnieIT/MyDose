from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Medication, Medication_drugs,Reminder
       # Create your views here.

def home (request) :
    return render(request, 'MyDose/home.html')



              #show user medication in a list
class MedicationListView(LoginRequiredMixin, ListView):
    model = Medication
#     template_name = ""
    def get(self, request, *args, **kwargs):
        all_medications = Medication.objects.filter(User_id = request.user)
        return render(request, "MyDose/medication.html", {"all_medications": all_medications})
         

         #show user medication drugs  in a list
class MedicationDrugsListView(LoginRequiredMixin, ListView):
    model = Medication_drugs
#     template_name = ""
    def get(self, request, *args, **kwargs):
        all_med_drugs = Medication_drugs.objects.filter(med_id__User_id = request.user)
        print(all_med_drugs)
        return render(request, "MyDose/MedicationDrugs.html", {"all_med_drugs": all_med_drugs})

             #show user reminders in a list

class ReminderListView(LoginRequiredMixin, ListView):

    model = Reminder
#     template_name = ""
    def get(self, request, *args, **kwargs):
        all_Reminders = Reminder.objects.filter(from_med_drugs__id = request.user)
        return render(request, "MyDose/MedicationDrugs.html", {"all_Reminders": all_Reminders})

            

