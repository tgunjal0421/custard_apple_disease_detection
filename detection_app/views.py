from django.shortcuts import render, redirect

# detection_app/views.py
from .forms import ImageUploadForm
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os
from collections import defaultdict
from .models import PredictionHistory
from django.contrib.auth.decorators import login_required

# Store disease counts (in-memory, or you can use a database)
disease_counts = defaultdict(int)

# Load your trained model (only once at app startup)
model = load_model(os.path.join('detection_app', 'models', 'model.h5'))

model_metrics = {
    'accuracy': 0.91,
    'precision': 0.91,
}

def home(request):
    """Render the homepage with a link to the upload page."""
    return render(request, 'home.html')

@login_required
def predict(request):
    """Handle the uploaded image and make predictions."""
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Retrieve the uploaded image
            image = form.cleaned_data['image']

            # Preprocess the image to fit the model's input
            img = Image.open(image).resize((128, 128))
            img_array = np.array(img) / 255.0  # Normalize the pixel values
            img_array = img_array.reshape(1, 128, 128, 3)  # Add batch dimension

            # Make prediction using the model
            prediction = model.predict(img_array)
            confidence = np.max(prediction) * 100  # Convert to percentage
            class_index = np.argmax(prediction)

            # Map the prediction index to disease names
            class_names = [
                'Anthracnose', 'Blank Canker', 'Diplodia Rot', 
                'Healthy', 'Leaf Spot on Fruit', 
                'Leaf Spot on Leaves', 'MealyBug'
            ]
            result = class_names[class_index]
            
            # Increment the disease count
            disease_counts[result] += 1
            
            # Save prediction to the database
            PredictionHistory.objects.create(image=image, result=result, confidence=confidence)

            
            # Render the result page with performance metrics
            return render(request, 'result.html', {
                'result': result, 
                'confidence': np.max(prediction) * 100, 
                'metrics': model_metrics
            })


    else:
        form = ImageUploadForm()

    return render(request, 'upload.html', {'form': form})

@login_required
def history(request):
    """Display all previous predictions."""
    predictions = PredictionHistory.objects.all().order_by('-timestamp').filter(user=user_login)
    return render(request, 'history.html', {'predictions': predictions})


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# User Registration
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            try:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'User registered successfully!')
                return redirect('login')
            except:
                messages.error(request, 'Username already exists.')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'register.html')

# User Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'login.html')

# User Logout
def user_logout(request):
    logout(request)
    return redirect('login')

