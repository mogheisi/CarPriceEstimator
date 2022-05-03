from django.urls import path
from .views import index, Estimator

urlpatterns = [
    path('', index, name='index'),
    path('Estimate/', Estimator.as_view(), name='Estimate'),
]
