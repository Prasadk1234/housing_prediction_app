import email
from email import message
from typing import Required
from django import forms
from django.contrib.auth.admin import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.forms import widgets

class UserRegistrationFrom(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model=User
        fields = ('username','email','password1','password2')


# class FeedbackForm(forms.Form):

#     name = forms.CharField(
#         max_length=100, 
#         required=True,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter your full name'
#         })
#     )
#     email = forms.EmailField(
#         required=True,
#         widget=forms.EmailInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter your email address'
#         })
#     )
#     feedback_type = forms.ChoiceField(
#         choices=[
#             ('', 'Select feedback type'),
#             ('prediction_accuracy', 'Prediction Accuracy'),
#             ('user_interface', 'User Interface'),
#             ('features', 'Features & Functionality'),
#             ('performance', 'Performance & Speed'),
#             ('suggestions', 'Suggestions & Ideas'),
#             ('bug_report', 'Bug Report'),
#             ('general', 'General Feedback')
#         ],
#         required=True,
#         widget=forms.Select(attrs={
#             'class': 'form-control'
#         })
#     )
#     rating = forms.ChoiceField(
#         choices=[
#             ('', 'Rate your experience'),
#             ('5', '⭐⭐⭐⭐⭐ Excellent'),
#             ('4', '⭐⭐⭐⭐ Very Good'),
#             ('3', '⭐⭐⭐ Good'),
#             ('2', '⭐⭐ Fair'),
#             ('1', '⭐ Poor')
#         ],
#         required=True,
#         widget=forms.Select(attrs={
#             'class': 'form-control'
#         })
#     )
#     message = forms.CharField(
#         widget=forms.Textarea(attrs={
#             'class': 'form-control',
#             'placeholder': 'Share your detailed feedback about the housing prediction system...',
#             'rows': 5
#         }),
#         required=True
#     )

