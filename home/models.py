from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class IssueReport(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Not Completed'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Done'),
    ]

    citizen = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    image_before = models.ImageField(upload_to='issues/before/')
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    image_after = models.ImageField(upload_to='issues/after/', null=True, blank=True)

    # --- NEW ADDITION: UPVOTES ---
    # This stores a list of Users who liked this report
    upvotes = models.ManyToManyField(User, related_name='upvoted_reports', blank=True)

    def __str__(self):
        return f"{self.description[:20]} - {self.status}"
    
    # Helper to count total votes
    def total_upvotes(self):
        return self.upvotes.count()