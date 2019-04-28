from django.urls import path
from MyDose import views
app_name = "medication"
urlpatterns = [
    path("", views.home, name="home"),
    path("my_medication/", views.MedicationListView.as_view(), name="my-medication"),
    path("my_medication_drugs/", views.MedicationDrugsListView.as_view(), name="my_medication_drugs"),
    path("reminders/", views.ReminderListView.as_view(), name="reminders"),
]