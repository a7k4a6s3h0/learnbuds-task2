from django import forms
from .models import Registration
from manage_accounts.models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['event']  # Since the user is automatically assigned, only event is required

        widgets = {
            'event': forms.HiddenInput()  # Event will be passed in the form as hidden input
        }


class UpdateRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['status']  # We only allow the status field to be updated

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget = forms.Select(choices=Registration.STATUS_CHOICES)


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # Add any fields you want to update
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # You can customize the fields' attributes (e.g., adding classes)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})        