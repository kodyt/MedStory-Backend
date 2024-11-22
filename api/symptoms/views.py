from symptoms.models import User, Symptom, UserSymptomLog, Diagnosis
from symptoms.serializers import SymptomSerializer, UserSerializer, DiagnosisSerializer, PatientSymptomSerializer, PatientMedicationSerializer, ReminderSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
import datetime


def get_symptoms(request):
    # invoke serializer and return to client
    data = Symptom.objects.all()
    serializer = SymptomSerializer(data, many=True)
    return JsonResponse({'symptoms': serializer.data})


@api_view(['POST'])
def add_general_symptom_log(request):
    '''Logs Numerical symptoms'''
    if request.method == 'POST':
        symptom_name = request.data.get("s_id", "").lower()
        if not symptom_name:
            return Response({"message": "Symptom name (s_id) is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        unit = request.data.get("unit", "").lower()
        if not unit:
            unit = "mmhg" # placeholder until we determine what this is


        symptom_obj, created = Symptom.objects.get_or_create(
            name=symptom_name,
            defaults={
                "description": request.data.get("description", "User created symptom."),
                "category": request.data.get("category", "numerical"),
                "Units": request.data.get("units", unit) # How should we specify this if it's not in the database
            }
        )
        diagnoses = request.data.get('diagnosis', []) 
        # Have to get the authentication user_id from the cookies somehow or frontend passes id?
        user = User.objects.get(id=1)

        log = UserSymptomLog.objects.create(
            user=user,
            severity=request.data["severity"],
            onset_time=request.data["onset_time"],
            modified_time= datetime.datetime.now(),
            notes= request.data["notes"],
            symptom_id=symptom_obj.id,
            is_numerical=symptom_obj.category == "numerical"
            )
        # Add diagnoses (if any)
        for diagnosis_name in diagnoses:
            diagnosis, created = Diagnosis.objects.get_or_create(name=diagnosis_name, user_id=user.id)
            log.diagnoses.add(diagnosis)
        return JsonResponse({'message': 'Symptom log created successfully', 'log_id': log.id}, status=201)

        # reminders = {
        #     "frequency": int(request.data["freq"]),
        #     "unit": request.data["remind_times"],
        #     "text": "Example reminder text"
        # }

        # serializer = PatientSymptomSerializer(data=symptom_data)
        # if serializer.is_valid():
        #     serializer.save()  # Save the data using the serializer's create method
        #     return Response({'message': 'Data saved successfully!'}, status=status.HTTP_201_CREATED)
        # else:
        #     return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        # reminder_serializer = ReminderSerializer(data=reminders)
        # if serializer.is_valid:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': "Invalid request"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def add_numerical_symptom_log(request):
    '''Logs Numerical symptoms'''
    if request.method == 'POST':
        symptom_name = request.data.get("s_id", "").lower()
        if not symptom_name:
            return Response({"message": "Symptom name (s_id) is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        unit = request.data.get("unit", "").lower()
        if not unit:
            unit = "mmhg" # placeholder until we determine what this is


        symptom_obj, created = Symptom.objects.get_or_create(
            name=symptom_name,
            defaults={
                "description": request.data.get("description", "User created symptom."),
                "category": request.data.get("category", "generic"),
                "Units": request.data.get("units", unit) # How should we specify this if it's not in the database
            }
        )
        diagnoses = request.data.get('diagnosis', []) 
        # Have to get the authentication user_id from the cookies somehow or frontend passes id?
        user = User.objects.get(id=1)

        log = UserSymptomLog.objects.create(

            # FIGURE OUT WHAT VALUES ARE WHAT IN THE FRONTEND AND WHERE TO SAVE IT
            user=user,
            onset_time=request.data["onset_time"],
            modified_time= datetime.datetime.now(),
            notes= request.data["notes"],
            symptom_id=symptom_obj.id,
            is_numerical=symptom_obj.category == "numerical",
            value=request.data["value"],
            unit=unit,
            )
        # reminder_serializer = ReminderSerializer(data=reminders)
        # "unit": request.data["unit"], # Going to be initialized in the frontend

        # Add diagnoses (if any)
        for diagnosis_name in diagnoses:
            diagnosis, created = Diagnosis.objects.get_or_create(name=diagnosis_name, user_id=user.id)
            log.diagnoses.add(diagnosis)
        return JsonResponse({'message': 'Symptom log created successfully', 'log_id': log.id}, status=201)
    else:
        return Response({'message': "Invalid request"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

@api_view(['POST'])
def add_medication_log(request):

    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key to Users
    # med_id = models.ForeignKey(Medication, on_delete=models.CASCADE)  # Foreign key to Medications
    # dosage = models.CharField(max_length=255, null=True)  # Dosage of the medication
    # unit = models.CharField(null=True, max_length=50)  # Unit of dosage (e.g., "mg", "ml")
    # log_time = models.DateTimeField(null=True)  # Time the medication was taken
    # notes = models.TextField(blank=True, null=True)
    if request.method == 'POST':
        # need to find the m_id from the database
        m_id = 1
        # find user_id?
        symptom_data = {
            "med_id": m_id,
            "dosage": request.data["dosage"],
            "dosage": request.data['freq'],
            "log_time": request.data['onset_time'],
            "notes": request.data['notes'],
        }

        reminders = {
            "frequency": int(request.data["freq"]),
            "unit": request.data["remind_times"],
            "text": "Example reminder text"
        }
