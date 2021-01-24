from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render (request, 'generator/home.html')

def password(request):
    thepassword = ''
    length = int(request.GET.get('length',12))
    char = list('abcdefghijklmnopqrstuvwxyz')
    upcase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    specialCh = list('!@#$%^&*()_+=-?{}|[]\/')
    numb = list('1234567890')
    if request.GET.get('uppercase'):
        char.extend (upcase)
    if request.GET.get('special'):
        char.extend (specialCh)
    if request.GET.get('numbers'):
        char.extend (numb)
    for i in range(length):
      thepassword += random.choice(char)

    return render (request, 'generator/password.html',{'password':thepassword})