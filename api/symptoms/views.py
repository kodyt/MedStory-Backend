from symptoms.models import Symptom
from symptoms.serializers import SymptomSerializer, UserSerializer, DiagnosisSerializer, PatientSymptomSerializer, PatientMedicationSerializer, ReminderSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def symptoms(request):
    # invoke serializer and return to client
    data = Symptom.objects.all()
    serializer = SymptomSerializer(data, many=True)
    return JsonResponse({'symptoms': serializer.data})


@api_view(['POST'])
def add_symptom_log(request):
    
    if request.method == 'POST':
        print("Catching post request")
        print(request.data)
        symptom_data = {
            "s_id": request.data["s_id"],
            "severity": request.data["severity"],
            "onset_time": request.data["onset_time"],
            "type_of_pain": request.data["type_of_pain"],
            "diagnosis": request.data["diagnosis"],
            "notes": request.data["notes"],
        }

        reminders = {
            "frequency": int(request.data["freq"]),
            "unit": request.data["remind_times"],
            "text": "Example reminder text"
        }

        serializer = PatientSymptomSerializer(data=symptom_data)
        if serializer.is_valid():
            serializer.save()  # Save the data using the serializer's create method
            return Response({'message': 'Data saved successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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