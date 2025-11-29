from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from .models import IssueReport
from .serializers import IssueReportSerializer, UserRegistrationSerializer

# ===========================
#  PART A: THE API (JSON)
# ===========================

# 1. Login API
class CustomLoginView(ObtainAuthToken):
    permission_classes = [permissions.AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'is_admin': user.is_staff
        })

# 2. Register API
class CitizenRegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

# 3. Reports API (List & Create)
class IssueReportViewSet(viewsets.ModelViewSet):
    serializer_class = IssueReportSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return IssueReport.objects.filter(citizen=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(citizen=self.request.user)


# ===========================
#  PART B: THE HTML PAGES
# ===========================
def login_page(request):
    return render(request, 'home/login.html')

def dashboard_page(request):
    return render(request, 'home/dashboard.html')