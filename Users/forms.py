from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from MyDose.models import Medication,Medication_drugs,Medication_drugs,drug_period,time_period


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']

class MedUpdateForm(forms.ModelForm):
    class Meta:
        model =Medication
        fields = ['diagnosis']

class MedDrugsForm(forms.ModelForm):

    class Meta:
        model = Medication_drugs
        fields = ['drug_name','med_id', 'frequency','mode_of_administration','duration','quantity']


