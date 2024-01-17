from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from . import models
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django import forms
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
    
# def add_record(request):
#     return render(request, 'website/add_record.html', {})
    
class AddRecord(CreateView, LoginRequiredMixin):
    model = models.Record
    fields = '__all__'
    template_name = 'website/add_record.html'
    success_url = reverse_lazy('home')

class UpdateRecord(UpdateView, LoginRequiredMixin):
    model = models.Record
    fields = "__all__"
    template_name = "website/update_record.html"
    success_url = reverse_lazy('home')