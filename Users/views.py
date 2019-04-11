from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, MedUpdateForm,MedDrugsForm
from MyDose.models import Medication,Medication_drugs,Medication_drugs,drug_period


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
def updatemeds(request):
    if request.method == 'POST':
        med_form = MedUpdateForm(request.POST,instance= request.user)
        drugs_form = MedDrugsForm(request.POST)
        if med_form.is_valid() and drugs_form.is_valid():
            med1 =med_form.save(commit=False)
            med1.user_id = request.user
            med1.save()
            drugs_form.save()
            messages.success(request, f'Medication updated')
            return redirect('profile')


    else:
        med_form = MedUpdateForm(instance= request.user)
        drugs_form = MedDrugsForm()
        


    context ={
        'med_form': med_form,
        'drugs_form':drugs_form
    }
    return render(request, 'users/updatemeds.html',context)
@login_required
def today(request):
    
    return render(request, 'users/today.html')




