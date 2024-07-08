from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Historia
from .serializers import HistoriaSerializer, RespostaSerializer

class HistoriaListView(APIView):
    def get(self, request, format=None):
        historias = Historia.objects.all()
        serializer = HistoriaSerializer(historias, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = HistoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RespostaCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RespostaSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FilteredHistoriaListView(APIView):
    def get(self, request, format=None):
        historia = Historia.objects.get(id=request.id)
        serializer = HistoriaSerializer(historia, many=True)
        return Response(serializer.data)
