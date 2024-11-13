from symptoms.models import Symptom
from symptoms.serializers import SymptomSerializer, UserSerializer, DiagnosisSerializer, PatientSymptomSerializer, PatientMedicationSerializer, ReminderSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
import datetime


def symptoms(request):
    # invoke serializer and return to client
    data = Symptom.objects.all()
    serializer = SymptomSerializer(data, many=True)
    return JsonResponse({'symptoms': serializer.data})


@api_view(['POST'])
def add_symptom_log(request):
    # For numerical?
    if request.method == 'POST':
        symptom_obj = get_object_or_404(Symptom, name=request.data["s_id"].lower())


        # Have to get the authentication user_id from the cookies somehow
        symptom_data = {
            "s_id": symptom_obj.id,
            "is_numerical": symptom_obj.category == "Numerical",
            "severity": request.data["severity"],
            "onset_time": request.data["onset_time"],
            "modified_time": datetime.datetime.now(),
            "type_of_pain": request.data["type_of_pain"],
            "diagnosis": request.data["diagnosis"],
            "notes": request.data["notes"],
            "value": "",
            "unit": "",
        }

        # reminders = {
        #     "frequency": int(request.data["freq"]),
        #     "unit": request.data["remind_times"],
        #     "text": "Example reminder text"
        # }

        serializer = PatientSymptomSerializer(data=symptom_data)
        if serializer.is_valid():
            serializer.save()  # Save the data using the serializer's create method
            return Response({'message': 'Data saved successfully!'}, status=status.HTTP_201_CREATED)
        
        # reminder_serializer = ReminderSerializer(data=reminders)
        # if serializer.is_valid:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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


# @api_view(['POST'])
# def add_symptom_numerical_log(request):
    
#     if request.method == 'POST':

#         symptom_data = {
#             "s_id": request.data["s_id"],
#             "severity": request.data["severity"],
#             "onset_time": request.data["time"],
#             "type_of_pain": request.data["type_of_pain"],
#             "diagnosis": request.data["diagnosis"],
#             "notes": request.data["notes"],
#         }

#         reminders = {
#             "frequency": int(request.data["freq"]),
#             "unit": request.data["remind_times"],
#             "text": "Example reminder text"
#         }

#         serializer = PatientSymptomSerializer(data=symptom_data)
#         if serializer.is_valid():
#             # serializer.save()  # Save the data using the serializer's create method
#             return Response({'message': 'Data saved successfully!'}, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)