from django.shortcuts import render, redirect

def index(request):
	return render( request, 'main/index.html')

def about(request):
	return render( request, 'main/about.html')

def gethelp(request):
	return render( request, 'main/gethelp.html')

def contact(request):
	return render( request, 'main/contact.html')