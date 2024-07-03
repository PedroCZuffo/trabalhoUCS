from django.urls import path
from .views import *

urlpatterns = [
    path('historias/', HistoriaListView.as_view(), name='historia-list'),
    path('historia/', FilteredHistoriaListView.as_view(), name='historia-filtered'),
]