from django.contrib import admin
from symptoms.models import Symptom, User, Diagnosis, PatientSymptom, PatientMedication, Reminder

admin.site.register(Symptom)
admin.site.register(User)
admin.site.register(Diagnosis)
admin.site.register(PatientSymptom)
admin.site.register(PatientMedication)
admin.site.register(Reminder)