from django.db import models
from datetime import datetime

# list of symptoms MedStory allows user to track
class Symptom(models.Model):
    # Change these to be what data a single symptom holds
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class User(models.Model):
    first_name = models.CharField(max_length=1000) # longest first name is 747 characters?
    last_name = models.CharField(max_length=1000)
    gender = models.CharField(max_length=1) # M/F

    def __str__(self):
        return (self.first_name, self.last_name)

class Diagnosis(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PatientSymptom(models.Model):
    # id (primary key) automatically created
    onset_created = models.DateTimeField(default=datetime.now()) #TODO: do we need both timestamps?
    onset_modified = models.DateTimeField(auto_now_add=True)
    reminder = models.BooleanField(default=False) # if the user wants a reminder for this
    severity = models.IntegerField()
    description = models.CharField(max_length=1000) #TODO: change to absolute number
    diagnosis = models.ManyToManyField('Diagnosis')

    def __str__(self):
        return f"Patient Report at {self.time}"
    
class PatientMedication(models.Model):
    name = models.CharField(max_length=50) # longest medication name is 29 characters?
    dosage = models.FloatField()
    notes = models.CharField(max_length=1000)
    reminder = models.BooleanField(default=False) # if the user wants a reminder for this

    def __str__(self):
        return self.name

class Reminder(models.Model):
    time = models.DateTimeField()
    frequency = models.IntegerField() #TODO: figure out how to measure 
    text = models.CharField(max_length=1000)
    # a reminder can be associated with either a symptom or a medication
    # this way ensures that the reminder gets deleted when the associated symptom/medication is deleted
    symptom = models.ForeignKey(PatientSymptom, on_delete=models.CASCADE, null=True, blank=True)
    medication = models.ForeignKey(PatientMedication, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        # ensure that a reminder is only associated with one of symptom/medication
        if self.symptom and self.medication:
            raise ValueError("A reminder can only be associated with either a symptom or a medication, not both.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.text

    