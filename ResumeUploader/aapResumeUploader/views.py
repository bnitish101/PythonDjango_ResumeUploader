from django.shortcuts import render
from .models import Resume
from django.views.generic import ListView, CreateView, UpdateView, DateDetailView
from .forms import ResumeForm
# Create your views here.

class ResumeCreateView(CreateView):
    template_name = 'aapResumeUploader/home.html'
    model = Resume
    # fields = '__all__'
    form_class = ResumeForm