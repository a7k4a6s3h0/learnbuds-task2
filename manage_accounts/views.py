from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import RoleBasedLoginForm
from .permissions import RedirectAuthenticatedUserMixin

def landing(request):
    return render(request, 'landing_page/landing_pg.html')

class RoleBasedLoginView(RedirectAuthenticatedUserMixin, LoginView):
     template_name = "login.html"  
     authentication_form = RoleBasedLoginForm

     def form_valid(self, form):
          """
          Overriding form_valid to add role validation.
          """
          user = form.get_user()
          role = form.cleaned_data.get('role')

          # Role validation logic
          
          if (
               (role == 'admin' and user.is_staff) or 
               (role == 'organizer' and  getattr(user, 'role', None) == 'organizer') or 
               (role == 'attendee' and getattr(user, 'role', None) == 'attendee') or 
               (role == 'venue_manager' and getattr(user, 'role', None) == 'venue_manager')
          ):
               messages.success(self.request, f"Logged in as {role.capitalize()}!")
               login(self.request, user)
               return super().form_valid(form)
          else:
               messages.error(self.request, "Selected role does not match your account.")
               return redirect('login')  
        
     def get_success_url(self):
          """
          Redirect based on role after login.
          """
          role = self.request.POST.get('role')
          if role == 'admin':
               return reverse('admin_home')  
          elif role == 'organizer':
               return reverse('events_home') 
          elif role == 'attendee':
               return reverse('attendee_home')  
          elif role == 'venue_manager':
               return reverse('venue_home')  
          return reverse('/')  # Default redirection
     
class UserLogoutView(LogoutView):
    next_page = 'landing'  # Redirect to the landing page after logout