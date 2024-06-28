from django.contrib import admin
from .models import Form, InputNumber, InputText, InputTime, InputMultipleChoice

class InputNumberInline(admin.TabularInline):
    model = InputNumber
    fk_name = 'form'

class InputTextInline(admin.TabularInline):
    model = InputText
    fk_name = 'form'

class InputTimeInline(admin.TabularInline):
    model = InputTime
    fk_name = 'form'

class InputMultipleChoiceInline(admin.TabularInline):
    model = InputMultipleChoice
    fk_name = 'form'

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    inlines = [InputNumberInline, InputTextInline, InputTimeInline, InputMultipleChoiceInline]
    list_display = ('title', 'uuid')
