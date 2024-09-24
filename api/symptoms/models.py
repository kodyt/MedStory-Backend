from django.db import models

class Symptom(models.Model):
    # Change these to be what data a single symptom holds
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Illness(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PatientData(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    severity = models.IntegerField()
    description = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    illness  = models.ManyToManyField('illness')

    def __str__(self):
        return f"Patient Report at {self.time}"
    