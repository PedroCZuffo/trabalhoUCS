from django.shortcuts import render, redirect
from django.views import View
from .forms import FormForm, InputNumberForm, InputTextForm, InputTimeForm, InputMultipleChoiceForm
from .models import *

class CreateFormView(View):
    def get(self, request):
        form = FormForm()
        return render(request, 'create_form.html', {'form': form})

    def post(self, request):
        form = FormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form_list')
        return render(request, 'create_form.html', {'form': form})

class AddInputView(View):
    def get(self, request, form_id):
        input_type = request.GET.get('type')
        if input_type == 'number':
            form = InputNumberForm()
        elif input_type == 'text':
            form = InputTextForm()
        elif input_type == 'time':
            form = InputTimeForm()
        elif input_type == 'multiple_choice':
            form = InputMultipleChoiceForm()
        else:
            form = None

        return render(request, 'add_input.html', {'form': form})

    def post(self, request, form_id):
        input_type = request.POST.get('type')
        if input_type == 'number':
            form = InputNumberForm(request.POST)
        elif input_type == 'text':
            form = InputTextForm(request.POST)
        elif input_type == 'time':
            form = InputTimeForm(request.POST)
        elif input_type == 'multiple_choice':
            form = InputMultipleChoiceForm(request.POST)
        else:
            form = None

        if form and form.is_valid():
            input_instance = form.save(commit=False)
            input_instance.form_id = form_id
            input_instance.save()
            return redirect('form_detail', form_id=form_id)
        
        return render(request, 'add_input.html', {'form': form})
    
class ListFormView(View):
    def get(self, request):
        forms = Form.objects.all()
        return render(request, 'list_forms.html', {'forms': forms})
    
        
class RenderFormView(View):
    def get(self, request):
        id = request.GET["form_id"]
        form = Form.objects.get(id=id)
        return render(request, 'render_form.html', {'form': form})
    
class menu_inicial(View):
    def get(self, request):
        Historia.objects.all()