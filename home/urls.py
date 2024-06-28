from django.urls import path
from .views import *

urlpatterns = [
    path('form/new/', CreateFormView.as_view(), name='create_form'),
    path('form/<uuid:form_id>/add_input/', AddInputView.as_view(), name='add_input'),
    path('form/list/', ListFormView.as_view(), name="form_list"),
    path('form/render_form/', RenderFormView.as_view(), name="form_render")
]