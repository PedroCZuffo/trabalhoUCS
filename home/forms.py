from django import forms
from .models import Form, InputNumber, InputText, InputTime, InputMultipleChoice

class FormForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['title', 'description']

class InputNumberForm(forms.ModelForm):
    class Meta:
        model = InputNumber
        fields = ['label', 'required', 'min_value', 'max_value']

class InputTextForm(forms.ModelForm):
    class Meta:
        model = InputText
        fields = ['label', 'required', 'max_length']

class InputTimeForm(forms.ModelForm):
    class Meta:
        model = InputTime
        fields = ['label', 'required']

class InputMultipleChoiceForm(forms.ModelForm):
    class Meta:
        model = InputMultipleChoice
        fields = ['label', 'required', 'choices']
