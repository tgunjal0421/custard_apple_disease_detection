from django.db import models

# Create your models here.
# detection_app/models.py
from django.db import models

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='uploads/')  # Folder to store images
    uploaded_at = models.DateTimeField(auto_now_add=True)


class PredictionHistory(models.Model):
    image = models.ImageField(upload_to='uploads/')
    result = models.CharField(max_length=100)
    confidence = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.result} - {self.timestamp}"
