from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def loginPage(request):
	if(request.POST):
		# CHECK AND SAVE USER
		return HttpResponse("Form Submitted")
	msg = "This is Login Page"
	return HttpResponse(msg)

def registerPage(request):
	msg = "This is Register Page"
	return render(request, 'register.html', {})
