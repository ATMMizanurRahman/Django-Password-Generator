from django.shortcuts import render
from django.http import HttpResponse
import random 
# Create your views here.

def home(request):
	return render(request,'generator/home.html',{'password':'cj7cr7mahi'})

def eggs(request):
    return HttpResponse("<h1>Eggs are So Good!</h1>")	

def About(request):
	return render(request,'generator/About.html')

def password (request):
	 char=list('abcdefghijklmnopqrstuvwxyz')
	 if request.GET.get('uppercase'):
	 	char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	 if request.GET.get('special'):
	 	char.extend(list('!@#$%^&*()_+'))
     

     


	 thepassword=''
	 len=int(request.GET.get('length'))

	 if request.GET.get('numbers'):
	 	char.extend(list('1234567890'))

	 for x in range(len):
	 	thepassword +=random.choice(char)
	 return render(request,'generator/password.html',{'password':thepassword})    