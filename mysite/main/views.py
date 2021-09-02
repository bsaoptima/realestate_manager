from django.shortcuts import render, redirect
from .models import Tutorial, TutorialSeries, TutorialCategory, Asset
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm

'''This is where models and views are created'''

'''
def single_slug(request, single_slug):
    assets = [a.asset_slug for a in Asset.objects.all()]
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)

        series_url={}

        for m in matching_series.all():
            part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
            series_url[m] = part_one.tutorial_slug

        return render(request,
                      "main/category.html",
                      {"part_ones": series_url})

    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
    if single_slug in tutorials:
        this_tutorial= Tutorial.objects.get(tutorial_slug=single_slug)
        tutorial_from_series = Tutorial.objects.filter(tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by('tutorial_published')
        this_tutorial_idx = list(tutorial_from_series).index(this_tutorial)

        return render(request=request,
                      template_name='main/tutorial.html',
                      context={"tutorial":this_tutorial,
                               "sidebar":tutorial_from_series,
                               "this_tut_idx":this_tutorial_idx})

    return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")
'''

#Define the homepage
def homepage(request):
    return render(request=request, #allows you to reference things inside template like users, etc.
                  template_name="main/dashboard.html", #tells django where to find template
                  context={"asset": Asset.objects.all}) #categories is now a variable

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