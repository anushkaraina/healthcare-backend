from django.urls import path
from .views import *

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),

    path('patients/', PatientListCreateView.as_view()),
    path('patients/<int:pk>/', PatientDetailView.as_view()),

    path('doctors/', DoctorListCreateView.as_view()),
    path('doctors/<int:pk>/', DoctorDetailView.as_view()),

    path('mappings/', PatientDoctorMappingListCreateView.as_view()),
    path('mappings/<int:patient_id>/', PatientDoctorsByPatientView.as_view()),
    path('mappings/<int:pk>/', PatientDoctorMappingDeleteView.as_view()),
]
