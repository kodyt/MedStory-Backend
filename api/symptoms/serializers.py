from rest_framework import serializers
from symptoms.models import Symptom, Illness, PatientData

class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ['name']

class IllnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Illness
        fields = ['name']

class PatientDataSerializer(serializers.ModelSerializer):
    illness = IllnessSerializer(many=True)

    class Meta:
        model = PatientData
        fields = ['time', 'severity', 'description', 'notes', 'illness']

    def create(self, validated_data):
        print("Start create function")
        
        illness_data = validated_data.pop('illness', [])
        # Create the PatientData object
        patient_data = PatientData.objects.create(**validated_data)
        
        # Process each illness and associate it with the PatientData
        for illness_info in illness_data:
            illness, created = Illness.objects.get_or_create(**illness_info)
            patient_data.illness.add(illness)
        
        return patient_data