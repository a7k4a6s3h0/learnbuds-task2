from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from urllib.parse import urlparse

def get_user_home_url(user):

     URLS = {
          'organizer': 'events_home',
          'attendee': 'attendee_home',
          'venue_manager': 'venue_home'
     }
     if user.is_superuser:
          return 'admin_home'
     elif user.role in URLS:
          return URLS[user.role]
     else:
          return '404'


class RedirectAuthenticatedUserMixin(UserPassesTestMixin):
     def test_func(self):
          user = self.request.user
          
          print("user in RedirectAuthenticatedUserMixin")
          
          if not user.is_authenticated:
               return True

          
          return False

     def handle_no_permission(self):
         return redirect(reverse_lazy(get_user_home_url(self.request.user)))

class CheckRolePermission(UserPassesTestMixin):
     def test_func(self):
          user = self.request.user

          # Check if the user is authenticated
          if not user.is_authenticated:
               return False

          if user.is_superuser:
               return True

          # Define the allowed permissions for each role
          PERMISSIONS_ALLOWED = {
               'attendee': ['register_event', 'update_registration', 'delete_registration', 'update_profile'],
               'organizer': ['create_event', 'create_venue', 'manage_venue', 'manage_events', 'update_event', 'delete_event'],
               'venue_manager': ['update_venue', 'delete_venue', 'manage_availability', 'manage_bookings', 'update_booking', 'delete_booking', 'update_availability', 'delete_availability', 'venue_details']
          }

          # Get the name of the URL the user requested
          url_name = self.request.resolver_match.url_name

          # Check if the user's role has permissions for the requested URL
          if user.role in PERMISSIONS_ALLOWED:
               if url_name in PERMISSIONS_ALLOWED[user.role]:
                    return True  # User has permission

          # If no matching role or permission is found, deny access
          return False

     def handle_no_permission(self):
          # Redirect to login page or any other page if permission is denied
          return redirect(reverse_lazy('login'))
       