from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Historia
from .serializers import HistoriaSerializer

class HistoriaListView(APIView):
    def get(self, request, format=None):
        historias = Historia.objects.all()
        serializer = HistoriaSerializer(historias, many=True)
        return Response(serializer.data)

class FilteredHistoriaListView(APIView):
    def get(self, request, format=None):
        historia = Historia.objects.get(id=request.id)
        serializer = HistoriaSerializer(historia, many=True)
        return Response(serializer.data)
