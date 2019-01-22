from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse
from userapp.forms import UserForm


# Create your views here.
def employee_list(request):
	context = {}
	context['users'] = User.objects.all()
	context['title'] = 'Employees'
	return render(request, 'userapp/index.html', context)

def employee_details(request, id=None):
	context = {}
	context ['user'] = get_object_or_404(User, id=id)
	return render(request, 'userapp/details.html', context)

def employee_add(request):
	context = {}
	if request.method =='POST':
		user_form =UserForm(request, POST)
		context['user_form'] = user_form
		if user_form is valid():
			user_form.save()
			return HttpResponseRedirect(reverse('employee_list'))
		else:
			return render(request,'userapp/add.html', {"user_form":user_form})
	else:
		user_form =UserForm()
		return render(request,'userapp/add.html', {"user_form":user_form})

def employee_delete(request, id=None):
	user = get_object_or_404(User, id=id)
	if request.method =='POST':
		user.delete()
		return HttpResponseRedirect(reverse('employee_list'))
	else:
		context = {}
		context['user'] = user
		return render(request, 'userapp/delete.html', context)

def user_login(request):
	context = {}
	if request.method == "POST":
		pass
	else:
		return render(request, "auth/login.html", context)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user:
			login(request,user)
			return HttpResponseRedirect(reverse('success'))
		else:
			context ["error"] = "Provide valid value"
			return render(request, "auth/login.html", context)

def success(request):
	context = {}
	context['user'] = request.user
	return render(request, "auth/success.html", context)

def user_logout(request):
	if request.method == "POST":
		logout(request)
		return HttpResponseRedirect(reverse('user_login'))