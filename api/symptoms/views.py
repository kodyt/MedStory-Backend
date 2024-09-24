from symptoms.models import Symptom
from symptoms.serializers import SymptomSerializer, IllnessSerializer, PatientDataSerializer
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
        print("FDSJOFNDSION")
        print(request.data)

        serializer = PatientDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the data using the serializer's create method
            return Response({'message': 'Data saved successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
