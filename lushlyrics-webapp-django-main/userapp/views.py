from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def mylogin(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(request, username = username, password = password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			err_msg = "Invalid username or password"
			return render(request, 'login.html', {'error_message': err_msg})
	
	return render(request, 'login.html')

def register(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		# password1 = request.POST['password1']
		# password2 = request.POST['password2']

		if password1==password2:
			try: 
				user = User.objects.create_user(username = username, email = email)
				user.set_password(password1)
				user.is_active = True
				user.save()
				auth.login(request,user)
				return redirect('/')
			except: 
				error_msg = "Error creating account"
			return render(request, 'signup.html',{'error_message':error_msg})

		else:
			error_msg = "Password don't match."
			return render(request, 'signup.html',{'error_message':error_msg})

	return render(request, 'signup.html')

def mylogout(request):
	auth.logout(request)
	return redirect('login')