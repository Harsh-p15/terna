from rest_framework import serializers
from django.contrib.auth.models import User
from .models import IssueReport

# 1. Signup Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

# 2. Report Serializer
class IssueReportSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    date_reported = serializers.DateTimeField(source='created_at', read_only=True)

    class Meta:
        model = IssueReport
        fields = ['id', 'image_before', 'description', 'latitude', 'longitude', 'status', 'date_reported']