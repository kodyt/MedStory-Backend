from django.contrib import admin
import symptoms.models as models
from django.contrib.auth.admin import UserAdmin

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Symptom)
admin.site.register(models.Medication)
admin.site.register(models.Diagnosis)
admin.site.register(models.BodyLocations)
admin.site.register(models.Reminder)
admin.site.register(models.UserSymptomLog)
admin.site.register(models.UserMedicationLog)