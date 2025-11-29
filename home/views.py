from django.shortcuts import render

from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User  # <--- This was missing!
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import IssueReport
from .serializers import IssueReportSerializer, UserRegistrationSerializer

# 1. ViewSet for Reports (History & Upload)
class IssueReportViewSet(viewsets.ModelViewSet):
    serializer_class = IssueReportSerializer
    permission_classes = [IsAuthenticated]
    
    # --- ADD THIS LINE ---
    authentication_classes = [TokenAuthentication]
    # ---------------------

    def get_queryset(self):
        return IssueReport.objects.filter(citizen=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(citizen=self.request.user)

# 2. View for Registration (Sign Up)
class CitizenRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer

# 3. View for Login (Get Token)
class CustomLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'is_admin': user.is_staff
        })