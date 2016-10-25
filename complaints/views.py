from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

@login_required
def index(request):
	context = {}
	return render(request, 'complaints/index.html', context)

def user_login(request):
	context = {'invalid_login': None}

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			login(request, user)
			return HttpResponseRedirect(reverse('index'))
		else:
			context['invalid_login'] = True

	return render(request, 'complaints/login.html', context)