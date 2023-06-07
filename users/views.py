from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            # try:
            #     user = User.objects.get(username=username)
            # except:
            #     messages.error(request, 'Username does not exist')

            # Checks in the database if the username and password match
            user = authenticate(request, username=username, password=password)

            # Check if the user is exist
            if user is not None:
                """
                Creates a user session in the database in the user 
                table and a session data will be added in the browser
                """
                login(request, user)
                return redirect('profiles')
            else:
                messages.error(request, 'Username OR password is incorrect')
        else:
            messages.error(request, 'Username does not exist')

    return render(request, 'users/login_register.html')


def logoutUser(request):
    """
    This method will delete the session data from the database 
    and in the browser
    """
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # The post data is temporarily saving it so that you can modify the data before saving it
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Account was successfully created!')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'An error has occured during registration')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    # Get all skills except without empty description
    topSkills = profile.skill_set.exclude(description__exact="")
    # Get all skills with empty description
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topSkills': topSkills,
               'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {'profile': profile, 'skills': skills, 'projects': projects}
    return render(request, 'users/account.html', context)
