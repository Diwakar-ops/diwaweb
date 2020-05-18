from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import First
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def home(request):
    first=First.objects.filter(city='Chennai').order_by('-pub_date')[:1]
    solapur = First.objects.filter(city='Solapur').order_by('-pub_date')[:1]
    print(solapur)
    if request.method == 'POST':
        city=request.POST.get('city')
        print(city)
        if city == 'Chennai':
            first = First.objects.filter(city='Chennai').order_by('-pub_date')[:1]
            return render(request, 'calc/home.html', {'first':first})
        else:

            print(solapur)
            return render(request,'calc/sola.html',{'solapur':solapur})


    return render(request, 'calc/home.html', {'first':first})

def detail(request):
    if request.method == 'POST':
        city=request.POST.get('city')
        print(city)
        if city == 'Chennai' or 'chennai':
            first = First.objects.filter(city='Solapur').order_by('-pub_date')[:1]
            return render(request,'calc/home.html')
        else:
            solapur=First.objects.filter(city='Solapur').order_by('-pub_date')[:1]
            print(solapur)
            return render(request,'calc/sola.html',{'solapur':solapur})
def chennai_past(request):
    chenn=First.objects.filter(city='Chennai')
    return render(request,'calc/chennai_past.html',{'chennais':chenn})
def solapur_past(request):
    s=First.objects.filter(city='Solapur')
    return render(request,'calc/solapur_past.html',{'solas':s})
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            login(request, user)
            messages.success(request,f"New account created:{username}")
            return redirect("")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")


    form=UserCreationForm

    return render(request, 'calc/form.html', {'form':form})




