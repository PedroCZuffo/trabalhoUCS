from django.db import models
import uuid

class Form(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.title

class InputBase(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    required = models.BooleanField(default=True)

    class Meta:
        abstract = True

class InputNumber(InputBase):
    min_value = models.IntegerField(null=True, blank=True)
    max_value = models.IntegerField(null=True, blank=True)
    
    form = models.ForeignKey(Form, related_name='input_numbers', on_delete=models.CASCADE)

class InputText(InputBase):
    max_length = models.IntegerField(null=True, blank=True)
    
    form = models.ForeignKey(Form, related_name='input_texts', on_delete=models.CASCADE)

class InputTime(InputBase):
    form = models.ForeignKey(Form, related_name='input_times', on_delete=models.CASCADE)

class InputMultipleChoice(InputBase):
    choices = models.TextField(help_text="Insira as opções separadas por vírgulas")

    form = models.ForeignKey(Form, related_name='input_multiple_choices', on_delete=models.CASCADE)

    def get_choices(self):
        return self.choices.split(',')


class Historia(models.Model):
    titulo = models.CharField(max_length=255)
    image = models.ImageField()

class Pergunta(models.Model):
    options = [
        "multiplaEscolha",
        "alternativa",
        "escala",
        "descritiva"        
    ]

    id = models.IntegerField(primary_key=True)
    tipo = models.IntegerField(null=True, blank=True)
    titulo = models.CharField(max_length=255)
    texto = models.CharField(max_length=255)
    historia = Historia()

class Botao(models.Model):
    id = models.IntegerField(primary_key=True)
    texto = models.CharField(max_length=255)
    pergunta = Pergunta()

