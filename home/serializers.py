from rest_framework import serializers
from .models import Historia, Pergunta, Botao, Resposta

class BotaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Botao
        fields = ['id', 'texto']

class PerguntaSerializer(serializers.ModelSerializer):
    botoes = BotaoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Pergunta
        fields = ['id', 'titulo', 'texto', 'botoes']

    def create(self, validated_data):
        botoes_data = validated_data.pop('botoes')
        pergunta = Pergunta.objects.create(**validated_data)
        for botao_data in botoes_data:
            Botao.objects.create(pergunta=pergunta, **botao_data)
        return pergunta

class HistoriaSerializer(serializers.ModelSerializer):
    perguntas = PerguntaSerializer(many=True, read_only=True)

    class Meta:
        model = Historia
        fields = ['titulo', 'image', 'perguntas']

    def create(self, validated_data):
        perguntas_data = validated_data.pop('perguntas')
        historia = Historia.objects.create(**validated_data)
        for pergunta_data in perguntas_data:
            botoes_data = pergunta_data.pop('botoes')
            pergunta = Pergunta.objects.create(historia=historia, **pergunta_data)
            for botao_data in botoes_data:
                Botao.objects.create(pergunta=pergunta, **botao_data)
        return historia

class RespostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resposta
        fields = ['id', 'texto', 'pergunta']