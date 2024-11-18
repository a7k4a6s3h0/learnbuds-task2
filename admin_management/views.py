from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseForbidden
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from manage_accounts.models import User 
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import FormView
from .forms import UserCreationForm, UserUpdateForm
from manage_accounts.permissions import CheckRolePermission, get_user_home_url

# Create your views here.

def admin_home(request):
    # url = get_user_home_url(request.user)
    # if url:
    #     return redirect(url)
    return render(request, 'admin_home.html')


class CreateUserView(CheckRolePermission, FormView):
    """
    Class-based view to handle user creation.
    """
    template_name = 'create_user.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('admin_home')  


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)



class UpdateUserView(CheckRolePermission, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'update_user.html'

    def form_valid(self, form):
        form.save()
        return redirect('admin_home')  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        USERID = self.kwargs.get('pk')
        print(USERID,"id.......................")
        context['user'] = User.objects.get(id=USERID)  
        return context


def delete_user(request, user_id):
    # Instantiate CheckRolePermission to check permissions
    # permission_check = CheckRolePermission()
    
    
    # if not permission_check.test_func():
    #     return HttpResponseForbidden("You do not have permission to delete users.")
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, 'User deleted successfully!')
    return redirect('admin_home')


def view_users(request):
    # Instantiate CheckRolePermission to check permissions
    # permission_check = CheckRolePermission()
    
    # if not permission_check.test_func():
    #     return HttpResponseForbidden("You do not have permission to access this page.")
    users = User.objects.all()
    return render(request, 'view_users.html', {'users': users})