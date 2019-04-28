from django.contrib import admin

# Register your models here.

from .models import Medication,Medication_drugs


class MedicationAdmin(admin.ModelAdmin):
    list_display=['Med_date', 'diagnosis','is_active' ]
admin.site.register(Medication, MedicationAdmin)

class Medication_drugsAdmin(admin.ModelAdmin):
    list_display=['med_id', 'drug_name','frequency', 'mode_of_administration','duration','quantity' ]
admin.site.register(Medication_drugs, Medication_drugsAdmin)


 