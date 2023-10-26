from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')
def password(request):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    thepassword = ''
    if request.GET.get('uppercase'):
        alphabet.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        alphabet.extend(list('!@#$%^S*()*)'))
    if request.GET.get('numbers'):
        alphabet.extend(list('0123456789'))
    length = int(request.GET.get('length',12))
    for i in range(length):
        thepassword += random.choice(alphabet)

    return render(request, 'generator/password.html', {'password':thepassword})

def aboutme(request):
    return  render(request, 'generator/aboutme.html')
