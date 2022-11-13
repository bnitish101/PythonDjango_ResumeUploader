from django.urls import path


from . import views
urlpatterns = [
    path('/', views.ResumeCreateView.as_view(), name='resume'),
    path('/candidate_detail/<slug:pk>', views.CandidateDetailView.as_view(), name='candidate_detail'),
]