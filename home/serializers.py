from rest_framework import serializers
from .models import Historia, Pergunta, Botao

class BotaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Botao
        fields = ['id', 'texto']

class PerguntaSerializer(serializers.ModelSerializer):
    botoes = BotaoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Pergunta
        fields = ['id', 'titulo', 'texto', 'botoes']

class HistoriaSerializer(serializers.ModelSerializer):
    perguntas = PerguntaSerializer(many=True, read_only=True)

    class Meta:
        model = Historia
        fields = ['titulo', 'image', 'perguntas']
