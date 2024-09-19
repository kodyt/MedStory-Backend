from django.db import models

class Symptom(models.Model):
    # Change these to be what data a single symptom holds
    name = models.CharField(max_length=100)
    severity = models.CharField(max_length=100)
    