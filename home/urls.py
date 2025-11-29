from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# API Router
router = DefaultRouter()
router.register(r'reports', views.IssueReportViewSet, basename='reports')

urlpatterns = [
    # --- HTML PAGES (Frontend) ---
    path('login/', views.login_page, name='page_login'),
    path('dashboard/', views.dashboard_page, name='page_dashboard'),

    # --- API ENDPOINTS (Backend) ---
    path('api/login/', views.CustomLoginView.as_view()),
    path('api/register/', views.CitizenRegisterView.as_view()),
    path('api/', include(router.urls)),
]