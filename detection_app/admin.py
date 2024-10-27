from django.contrib import admin

# Register your models here.
from .models import PredictionHistory, DiseaseInfo

admin.site.register(PredictionHistory)
admin.site.register(DiseaseInfo)
