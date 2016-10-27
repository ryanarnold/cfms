from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from complaints.forms import ComplaintForm
from complaints.models import Complaint
from django import forms
import re, datetime

@login_required
def index(request):
	context = {}
	return render(request, 'complaints/index.html', context)

def user_login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('index'))

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

def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

def new_complaint(request):
	if request.method == 'POST':
		form = ComplaintForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
		else:
			print(form.errors)

	try:
		year_re = re.compile(r'^[0-9]{4}')
		last_number = int(re.sub(year_re, '', str(Complaint.objects.order_by('-id')[0].number)))
		new_number = str(datetime.date(2000, 1, 1).today().year) + ('0' * (4 - len(str(last_number)))) + str(last_number + 1)
	except IndexError:
		new_number = str(datetime.date(2000, 1, 1).today().year) + '0001'
	form = ComplaintForm({'number': new_number})

	context = {'form': form}
	return render(request, 'complaints/new_complaint.html', context)

def search_complaint(request):
	context = {}

	if request.method == 'GET' and request.GET.get('submit') != None:
		number = request.GET.get('number')

		results = Complaint.objects.filter(number__contains=number)

		context['results'] = results

	return render(request, 'complaints/search_complaint.html', context)