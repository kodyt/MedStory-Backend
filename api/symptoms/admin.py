from django.contrib import admin
from symptoms.models import Symptom, Illness, PatientData

admin.site.register(Symptom)
admin.site.register(Illness)
admin.site.register(PatientData)