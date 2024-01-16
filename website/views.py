from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from . import models
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    records = models.Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged In")
            return redirect('home')
        else:
            messages.success(request, "There Was an error Loggin in. Please Try again.")
            return redirect('home')
    else:
        
        return render(request, 'website/home.html', {'records': records})


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out")
    return redirect('home')

def simple_view(request):
    return render(request, 'website/simple_view.html')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(username=username, password=password1)
            login(request, user)
            messages.success(request, "You have Succesfully Registered. Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})

class RecordView(DetailView, LoginRequiredMixin):
    model = models.Record
    template_name = 'website/record.html'


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = models.Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to do that operation")
        return redirect('home')