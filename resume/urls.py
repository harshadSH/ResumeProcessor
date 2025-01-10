from django.urls import path
from .views import *

urlpatterns = [
    path('extract_resume/', ResumeExtractionView.as_view(), name='extract_resume'),
    path('upload-resume/', upload_resume, name='upload_resume'),

]
