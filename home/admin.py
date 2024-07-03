from django.contrib import admin
from .models import Historia, Pergunta, Botao

class BotaoInline(admin.TabularInline):
    model = Botao
    extra = 1

class PerguntaInline(admin.TabularInline):
    model = Pergunta
    extra = 1

class HistoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'image')
    inlines = [PerguntaInline]

class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'texto', 'historia', 'tipo')
    inlines = [BotaoInline]

class BotaoAdmin(admin.ModelAdmin):
    list_display = ('texto', 'pergunta')

admin.site.register(Historia, HistoriaAdmin)
admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Botao, BotaoAdmin)
