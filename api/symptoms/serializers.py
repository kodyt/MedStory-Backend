from rest_framework import serializers
from symptoms.models import Symptom, User, Diagnosis, PatientSymptom, PatientMedication, Reminder

class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender']

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ['name', 'user']

class PatientSymptomSerializer(serializers.ModelSerializer):
    diagnosis = DiagnosisSerializer(many=True)

    class Meta:
        model = PatientSymptom
        fields = ['onset_created', 'onset_modified', 'set_reminder', 'severity', 'description', 'diagnosis']

    def create(self, validated_data):
        print("Start create function")
        
        diagnosis_data = validated_data.pop('diagnosis', [])
        # Create the PatientSymptom object
        patient_symptom = PatientSymptom.objects.create(**validated_data)
        
        # Process each diagnosis and associate it with the PatientData
        for diagnosis_info in diagnosis_data:
            diagnosis, created = Diagnosis.objects.get_or_create(**diagnosis_info)
            patient_symptom.diagnosis.add(diagnosis)
        
        return patient_symptom
    

class PatientMedicationSerializer(serializers.ModelSerializer):
    diagnosis = DiagnosisSerializer(many=True)

    class Meta:
        model = PatientMedication
        fields = ['name', 'dosage', 'notes', 'set_reminder', 'diagnosis']

    def create(self, validated_data):
        print("Start create function")
        
        diagnosis_data = validated_data.pop('diagnosis', [])
        # Create the PatientSymptom object
        patient_medication = PatientMedication.objects.create(**validated_data)
        
        # Process each diagnosis and associate it with the PatientData
        for diagnosis_info in diagnosis_data:
            diagnosis, created = Diagnosis.objects.get_or_create(**diagnosis_info)
            patient_medication.diagnosis.add(diagnosis)
        
        return patient_medication
    
class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['time', 'frequency', 'text', 'symptom', 'medication']
