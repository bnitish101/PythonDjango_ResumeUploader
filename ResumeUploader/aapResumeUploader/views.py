from django.shortcuts import render
from .models import Resume
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .forms import ResumeForm
# Create your views here.

class ResumeCreateView(CreateView):
    template_name = 'aapResumeUploader/home.html'
    model = Resume
    # fields = '__all__'
    form_class = ResumeForm
    success_url = '/resume/'
    resume_list = Resume.objects.all()
    extra_context = {'resume_list': resume_list, 'my_data':'test'}
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)    
    #     context["resume_list"] = Resume.objects.all()
    #     return context


class CandidateDetailView(DetailView):
    # template_name = 'aapResumeUploader/candidate_detail.html'
    model = Resume