
from django.shortcuts import render

from django.template import loader
def index(request):
  return render(request,'index.html');


def pricing(request):
  return render(request,'pricing.html');

def contact(request):
  return render(request,'contact.html');

def signin(request):
  return render(request,'signin.html');


def signup(request):
  return render(request,'signup.html');

def subscribe(request):
  return render(request,'subscribe.html'); 
 


