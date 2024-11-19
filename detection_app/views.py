from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os
from collections import defaultdict
from .models import PredictionHistory, DiseaseInfo

# Load your trained model (only once at app startup)
model = load_model(os.path.join('detection_app', 'models', 'model.h5'))

# In-memory storage for model performance metrics and disease counts
model_metrics = {'accuracy': 0.91, 'precision': 0.91}
disease_counts = defaultdict(int)

def home(request):
    """Render the homepage."""
    return render(request, 'home.html')

@login_required
def predict(request):
    """Handle image upload and make predictions."""
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Retrieve and preprocess the uploaded image
            image = form.cleaned_data['image']
            img = Image.open(image).resize((128, 128))
            img_array = np.array(img) / 255.0  # Normalize the pixel values
            img_array = img_array.reshape(1, 128, 128, 3)  # Add batch dimension

            # Make prediction
            prediction = model.predict(img_array)
            confidence = np.max(prediction) * 100  # Convert to percentage
            class_index = np.argmax(prediction)

            # Map prediction index to disease names
            class_names = [
                'Anthracnose', 'Blank Canker', 'Diplodia Rot',
                'Healthy', 'Leaf Spot on Fruit',
                'Leaf Spot on Leaves', 'MealyBug'
            ]
            result = class_names[class_index]

            # Update disease count and save prediction to the database
            disease_counts[result] += 1
            PredictionHistory.objects.create(
                user=request.user,  # Link prediction to logged-in user
                image=image,
                result=result,
                confidence=confidence
            )
            
            # Fetch disease info
            disease_info = DiseaseInfo.objects.get(disease_name=result)

            return render(request, 'result.html', {
                'result': result,
                'confidence': confidence,
                'metrics': model_metrics,
                'disease_info': disease_info,
            })
    else:
        form = ImageUploadForm()

    return render(request, 'upload.html', {'form': form})

@login_required
def history(request):
    """Display the logged-in user's prediction history."""
    predictions = PredictionHistory.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'history.html', {'predictions': predictions})

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


def disease_info(request, disease_name):
    try:
        disease = DiseaseInfo.objects.get(disease_name=disease_name)
    except DiseaseInfo.DoesNotExist:
        disease = None
    
    return render(request, 'disease_info.html', {'disease': disease})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def settings(request):
    if request.method == 'POST':
        # Update user settings (e.g., username, email)
        username = request.POST.get('username')
        email = request.POST.get('email')
        
        request.user.username = username
        request.user.email = email
        request.user.save()

        messages.success(request, "Your settings have been updated.")
        return redirect('profile')

    return render(request, 'settings.html')
