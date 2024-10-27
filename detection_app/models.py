from django.db import models

# Create your models here.
# detection_app/models.py
from django.db import models

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='uploads/')  # Folder to store images
    uploaded_at = models.DateTimeField(auto_now_add=True)

from django.contrib.auth.models import User

class PredictionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    image = models.ImageField(upload_to='predictions/')
    result = models.CharField(max_length=100)
    confidence = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.result} - {self.timestamp}"

class DiseaseInfo(models.Model):
    disease_name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    cure = models.TextField()
    care_recommendations = models.TextField()
