from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required

# for authentication
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash,get_user_model
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
from django.core.exceptions import ValidationError

#send mail
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
UserModel=get_user_model()


# for register last

from django.db.models import Q
from django.core.paginator import Paginator
from django.core.mail import BadHeaderError
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext_lazy as _
# pagination
from django.core.paginator import Paginator
from django.http import JsonResponse


# for register last

from django.db.models import Q
from django.core.paginator import Paginator
from django.core.mail import BadHeaderError
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import gettext_lazy as _
# pagination
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from .models import StaffAndSuperuser




@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    messages.success(request, 'Logout Success')
    return redirect('login')


def loginuser(request):  
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful')                     
            return redirect('home') 
        else:
            messages.error(request, 'Invalid JISC ID or Password')
    else:
        form = AuthenticationForm()
    
    return render(request, 'authportal/login.html', {'form': form})




@login_required(login_url='login')
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Change Success')
            return redirect('login')  
    else:
        form = PasswordChangeForm(user=request.user) 
    return render(request, 'authportal/change_password.html', {'form':form}) 

