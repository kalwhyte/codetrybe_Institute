from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.admin import User
from .models import Admin
from .forms import AdminRegistrationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    return render(request, template_name="panel/index.html")


def welcome(request):
    return render(request, template_name="panel/index.html")


def loging(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    login(request, user)
                    return redirect('panel-adminpage')
                else:
                    # Return an 'invalid login' error message.
                    form.add_error('password', 'Invalid username or password')
            except User.DoesNotExist:
                form.add_error('username', 'Invalid username or password')
    else:
        form = AuthenticationForm()

    return render(request,'panel/login.html',{'form':form})


def admin(request):
    
    return render(request, template_name="panel/admin.html")

def register(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Admin.objects.create(user=user, phone_number=form.cleaned_data['phone_number'])
            return redirect('panel-adminpage')  
    else:
        form = AdminRegistrationForm()
    return render(request,"panel/register.html", {'form':form})