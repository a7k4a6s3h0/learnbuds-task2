from django import forms
from manage_accounts.models import User


class UserCreationForm(forms.ModelForm):
     class Meta:
          model = User
          fields = ['username', 'password', 'email', 'role']
          widgets = {
               'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
               'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
               'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
               'role': forms.Select(attrs={'class': 'form-control'}),
          }
    
     # Optionally, add password confirmation for better UX
     confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))
     
     def clean(self):
          cleaned_data = super().clean()
          password = cleaned_data.get('password')
          confirm_password = cleaned_data.get('confirm_password')
          
          if password != confirm_password:
               self.add_error('confirm_password', 'Passwords do not match')

          return cleaned_data
     

     def save(self, commit=True):
        # Use the `set_password` method to hash the password
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
     class Meta:
          model = User
          fields = ['username', 'email', 'password', 'role']
          widgets = {
               'username': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter username',
               }),
               'password': forms.PasswordInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter password',
               }),
               'email': forms.EmailInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter email',
               }),
               'role': forms.Select(attrs={
                    'class': 'form-control',
               }),
          }