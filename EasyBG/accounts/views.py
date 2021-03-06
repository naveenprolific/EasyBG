from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout
from accounts.forms import RegistrationForm

def register_view(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			return redirect('blogapp:list')
	else:
		form = RegistrationForm(None)
	context = {'form':form}
	return render(request,'accounts/signup.html',context) 

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request,user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:
				return redirect('blogapp:list')
	else:
		form = AuthenticationForm(None)
	context = {'form':form}
	return render(request,'accounts/login.html',context)


def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('blogapp:list')

