from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, MedUpdateForm,MedDrugsForm
from MyDose.models import Medication,Medication_drugs,Medication_drugs,drug_period, Reminder


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html', {'form':form} )
@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required   
def updatediagnosis(request):
    if request.method == 'POST':
        med_form = MedUpdateForm(request.POST)
        med_form.instance.User_id = request.user
        if med_form.is_valid():
            # med1 =med_form.save(commit=False)
            med_form.save()
            messages.success(request, f'Medication updated')
            return redirect('users:updatemeds')
    else:
        med_form = MedUpdateForm(instance= request.user)
    context ={
        'med_form': med_form,
    }
    return render(request, 'users/diagnosis.html',context)

@login_required   
def updatemeds(request):
    if request.method == 'POST':
        drugs_form = MedDrugsForm(request.POST)
        if drugs_form.is_valid():
            drugs_form.save()
            messages.success(request, f'Medication updated')
            return redirect('profile')


    else:
        drugs_form = MedDrugsForm()
    context ={
        'drugs_form':drugs_form
    }
    return render(request, 'users/updatemeds.html',context)
@login_required
def today(request):
    
    return render(request, 'users/today.html')


class CreateReminderView(LoginRequiredMixin, CreateView):
    model = Reminder
    fields =['from_diagnosis','from_med_drugs','reminder_time_morning','reminder_time_midday','reminder_time_evening']
    template_name = "users/create_reminder.html"

            



