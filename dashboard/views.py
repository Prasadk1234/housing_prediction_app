from django.shortcuts import render
from django.http import request
from django.shortcuts import redirect, render
from .forms import UserRegistrationFrom
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
import pickle
from num2words import num2words
from .forms import FeedbackForm
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime

with open("pune_price_model_lr_model.pkl", "rb") as f:
    loaded_model = pickle.load(f)

# Make prediction



def register_view(request):
    if request.method == "POST":
        form = UserRegistrationFrom(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationFrom()
    return render(request, 'registrations/register.html', {'form': form})



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registrations/login.html', {'form': form})

def predict_view(request):
    
    if request.method == 'POST':
        size = request.POST['size']
        total_sqft = request.POST['total_sqft']
        bath = request.POST['bath']
        balcony = request.POST['balcony']
        all_no_of_rooms = request.POST['all_no_of_rooms']

        size = int(size)
        total_sqft = float(total_sqft)
        bath = int(bath)
        balcony = int(balcony)
        all_no_of_rooms = int(all_no_of_rooms)

        new_preprocessed_data = [[size,total_sqft,bath,balcony,all_no_of_rooms]]
        
        prediction = loaded_model.predict(new_preprocessed_data)
        prediction = int(prediction[0])*100000
        to_words = num2words(prediction, lang='en_IN')
        

        context = {
            'result_numeric': prediction,
            'result_words': to_words
        }
        # y_pred = loaded_model.predict([])

        return render(request, 'registrations/predict.html',context)
    
    return render(request, 'registrations/predict.html')



def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            feedback_type = form.cleaned_data['feedback_type']
            rating = form.cleaned_data['rating']
            message = form.cleaned_data['message']

            # Create a detailed feedback message
            feedback_message = f"""
                Feedback Type: {feedback_type}
                Rating: {rating}
                From: {name} <{email}>

                Feedback Message:
                {message}
            """

            # Try to send email to your Gmail inbox
            try:
                send_mail(
                    subject=f"🏠 Housing Predictor Feedback: {feedback_type}",
                    message=feedback_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],  # Send to your Gmail inbox
                    fail_silently=False,  # Show errors if email fails
                )
                email_sent = True
            except Exception as e:
                # Log the error but don't break the form submission
                print(f"Email sending failed: {e}")
                email_sent = False

            # Store feedback in session for now (you can later save to database)
            if 'feedback_submissions' not in request.session:
                request.session['feedback_submissions'] = []
            
            feedback_data = {
                'name': name,
                'email': email,
                'feedback_type': feedback_type,
                'rating': rating,
                'message': message,
                'timestamp': str(datetime.now()),
                'email_sent': email_sent
            }
            
            request.session['feedback_submissions'].append(feedback_data)
            request.session.modified = True

            from django.contrib import messages
            if email_sent:
                messages.success(request, f'Thank you {name}! Your feedback has been submitted successfully and sent via email. We appreciate your input to improve our housing prediction system.')
            else:
                messages.success(request, f'Thank you {name}! Your feedback has been submitted successfully. We appreciate your input to improve our housing prediction system.')
            return redirect('feedback')

    else:
        form = FeedbackForm()
    return render(request, 'registrations/feedback.html', {'form': form})


