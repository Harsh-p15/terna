from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IssueReportViewSet, CustomLoginView, CitizenRegisterView

router = DefaultRouter()
router.register(r'reports', IssueReportViewSet, basename='user-reports')

urlpatterns = [
    # React hits: /api/home/login/
    path('login/', CustomLoginView.as_view(), name='api_login'),
    
    # React hits: /api/home/register/
    path('register/', CitizenRegisterView.as_view(), name='api_register'),
    
    path('', include(router.urls)),
]