from django.urls import path
from . import views
urlpatterns = [
    path('resume/', views.ResumeCreateView.as_view(), name='resume'),
]
