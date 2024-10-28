from rest_framework import serializers
from symptoms.models import Symptom, User, Diagnosis, UserSymptomLog, UserMedicationLog, Reminder

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
        model = UserSymptomLog
        fields = '__all__'


    def create(self, validated_data):
        print("Start create function")
        diagnosis_data = validated_data.pop('diagnosis', [])
        # Create the PatientSymptom object
        patient_symptom = UserSymptomLog.objects.create(**validated_data)
        
        # Process each diagnosis and associate it with the PatientData
        for diagnosis_info in diagnosis_data:
            diagnosis, created = Diagnosis.objects.get_or_create(**diagnosis_info)
            patient_symptom.diagnosis.add(diagnosis)
        
        return patient_symptom
    

class PatientMedicationSerializer(serializers.ModelSerializer):
    diagnosis = DiagnosisSerializer(many=True)

    class Meta:
        model = UserMedicationLog
        fields = '__all__'

    def create(self, validated_data):
        print("Start create function")
        
        diagnosis_data = validated_data.pop('diagnosis', [])
        # Create the PatientSymptom object
        patient_medication = UserMedicationLog.objects.create(**validated_data)
        
        # Process each diagnosis and associate it with the PatientData
        for diagnosis_info in diagnosis_data:
            diagnosis, created = Diagnosis.objects.get_or_create(**diagnosis_info)
            patient_medication.diagnosis.add(diagnosis)
        
        return patient_medication
    
class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        # fields = ['time', 'frequency', 'text', 'symptom', 'medication']
        fields = ['time', 'frequency', 'unit', 'text']
