from django.urls import path
from . import views

urlpatterns = [
    path('stucreate/',views.student_create),
]
