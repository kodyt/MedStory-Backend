from symptoms.models import Symptom
from symptoms.serializers import SymptomSerializer
from django.http import JsonResponse

def symptoms(request):
    # invoke serializer and return to client
    data = Symptom.objects.all()
    serializer = SymptomSerializer(data, many=True)
    return JsonResponse({'symptoms': "TESTES"})
    # return JsonResponse({'symptoms': serializer.data})
    # Error table doesn't exist yet

