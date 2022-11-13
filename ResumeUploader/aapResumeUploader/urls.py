from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('/', views.ResumeCreateView.as_view(), name='resume'),
    path('/candidate_detail/<slug:pk>', views.CandidateDetailView.as_view(), name='candidate_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)