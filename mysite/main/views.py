from django.shortcuts import render, redirect
from .models import Asset, People
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm

'''This is where models and views are created'''

CASHFLOW = Asset.objects.filter()

#Define the homepage
def homepage(request):
    return render(request=request, #allows you to reference things inside template like users, etc.
                  template_name="main/dashboard.html", #tells django where to find template
                  context={"assets": Asset.objects.all(),
                           "peoples": People.objects.all()} #assets is now a variable
    )

def show_assets(request):

    return render(request=request,
                  template_name="main/assets.html",
                  context={"assets": Asset.objects.all(),
                           "peoples": People.objects.all()}
    )


#Register function
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account created: {username}")
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request,
                  template_name="main/register.html",
                  context={"form": form})

#Used to log out
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

#Used to log in
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="main/login.html",
                  context={"form":form})