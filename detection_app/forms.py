# detection_app/forms.py
from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='Upload a leaf image for prediction')
