from django.db import models

class Historia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    image = models.ImageField()

class Pergunta(models.Model):
    MULTIPLA_ESCOLHA = 0
    ALTERNATIVA = 1
    ESCALA = 2
    DESCRITIVA = 3

    TIPO_CHOICES = [
        (MULTIPLA_ESCOLHA, "multiplaEscolha"),
        (ALTERNATIVA, "alternativa"),
        (ESCALA, "escala"),
        (DESCRITIVA, "descritiva")
    ]

    id = models.AutoField(primary_key=True)
    tipo = models.IntegerField(choices=TIPO_CHOICES, null=True, blank=True)
    titulo = models.CharField(max_length=255)
    texto = models.CharField(max_length=255)
    historia = models.ForeignKey(Historia, related_name='perguntas', on_delete=models.CASCADE, null=True, blank=True)

class Botao(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=255)
    pergunta = models.ForeignKey(Pergunta, related_name='botoes', on_delete=models.CASCADE, null=True, blank=True)
