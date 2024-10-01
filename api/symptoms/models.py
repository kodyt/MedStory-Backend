from django.db import models
from datetime import datetime
from django.utils import timezone
# list of symptoms MedStory allows user to track
class User(models.Model):
    # user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=1000, null=True) # longest first name is 747 characters?
    last_name = models.CharField(max_length=1000, null=True)
    gender = models.CharField(max_length=5, null=True) # M/F/Other
    email = models.EmailField(unique=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, null=True)
    dob = models.DateField(null=True) # Date of birth
    # allergies at some point

    def __str__(self):
        return (self.first_name, self.last_nameD)

class Symptom(models.Model):
    # Change these to be what data a single symptom holds
    # symptom_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    
    def __str__(self):
        return self.name
    

class Medication(models.Model):
    # m_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

class Diagnosis(models.Model):
    name = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class BodyLocations(models.Model):
    # body_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)

class Reminder(models.Model):
    # r_id = models.AutoField(primary_key=True)
    time = models.DateTimeField(null=True)
    frequency = models.IntegerField() #TODO: figure out how to measure 
    unit = models.IntegerField(default=0) # 0 = minutes, 1 = hours, 2 = days, 3 = weeks, 4 = months
    text = models.CharField(max_length=1000, null=True)
    # a reminder can be associated with either a symptom or a medication
    # this way ensures that the reminder gets deleted when the associated symptom/medication is deleted
    s_id = models.ForeignKey(Symptom, on_delete=models.CASCADE, null=True, blank=True)
    m_id = models.ForeignKey(Medication, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        # ensure that a reminder is only associated with one of symptom/medication
        if self.symptom and self.medication:
            raise ValueError("A reminder can only be associated with either a symptom or a medication, not both.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.text
    


class UserSymptomLog(models.Model):
    # log_id = models.AutoField(primary_key=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE) # To add once we do authentication
    s_id = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    severity = models.IntegerField(null=True)
    onset_time = models.DateTimeField(default=timezone.now)
    modified_time = models.DateTimeField(default=timezone.now)
    type_of_pain = models.JSONField(null=True)
    diagnosis = models.ManyToManyField('Diagnosis')
    notes = models.TextField(blank=True, null=True)

    value = models.IntegerField(null=True)
    unit = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f"Patient Report at {self.time}"
    
# class UserMedicationLog(models.Model):
#     name = models.CharField(max_length=50) # longest medication name is 29 characters?
#     dosage = models.FloatField()
#     notes = models.CharField(max_length=1000)
#     set_reminder = models.BooleanField(default=False) # if the user wants a reminder for this
#     diagnosis = models.ManyToManyField('Diagnosis')

#     def __str__(self):
#         return self.name

class UserMedicationLog(models.Model):
    # log_id = models.AutoField(primary_key=True)  # Integer primary key
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key to Users
    med_id = models.ForeignKey(Medication, on_delete=models.CASCADE)  # Foreign key to Medications
    dosage = models.CharField(max_length=255, null=True)  # Dosage of the medication
    unit = models.CharField(null=True, max_length=50)  # Unit of dosage (e.g., "mg", "ml")
    log_time = models.DateTimeField(null=True)  # Time the medication was taken
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Medication Log {self.log_id} for User {self.user_id}'