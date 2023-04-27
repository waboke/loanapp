from django.shortcuts import render,redirect
from .models import UserCreateForm
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, "home/index.html")

# Create your views here.
def home(request):
    return render(request, "home/home.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect('login')
    else:
        form = UserCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'home/signup.html', context)