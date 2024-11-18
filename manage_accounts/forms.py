from django import forms
from django.contrib.auth.forms import AuthenticationForm

class RoleBasedLoginForm(AuthenticationForm):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('organizer', 'Event Organizer'),
        ('attendee', 'Attendee'),
        ('venue_manager', 'Venue Manager'),
    ]

    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
        max_length=150,
        required=True,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
        required=True,
    )
