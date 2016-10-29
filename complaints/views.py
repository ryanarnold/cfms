from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from complaints.forms import ComplaintForm, UpdateComplaintForm, UserForm
from complaints.models import Complaint
from django import forms
import re, datetime

@login_required
def index(request):
	context = {}
	return render(request, 'complaints/index.html', context)

@login_required
def redirect_to_index(request):
	return HttpResponseRedirect(reverse('index'))

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

		context['number_retained'] = number

	return render(request, 'complaints/search_complaint.html', context)

def update_complaint(request, complaint_number):
	complaint2update = Complaint.objects.get(number=complaint_number)

	if request.method == 'POST':
		submit_type = request.POST.get('submit')

		if submit_type != 'discard':
			form = UpdateComplaintForm(data=request.POST, instance=complaint2update)
			complaint = form.save(commit=True)

			if submit_type == 'continue':
				return render(request, 'complaints/update_complaint.html', {'form': form})
			elif submit_type == 'search':
				return HttpResponseRedirect(reverse('search_complaint'))

	
	form = UpdateComplaintForm(instance=complaint2update)

	return render(request, 'complaints/update_complaint.html', {'form': form})

def users(request):
	results = User.objects.order_by('username')
	return render(request, 'complaints/users.html', {'results': results})

def add_user(request):
	user_form = UserForm()

	if request.method == 'POST':
		submit_type = request.POST.get('submit')
		
		if submit_type == 'discard':
			return HttpResponseRedirect(reverse('users'))
		else:
			# user_form = UserForm(data=request.POST)
			# user_form.save(commit=True)
			username = request.POST.get('username')
			password = request.POST.get('password')
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			user = User.objects.create_user(username=username, 
				password=password, 
				first_name=first_name, 
				last_name=last_name)

			if submit_type == 'another':
				return HttpResponseRedirect(reverse('add_user'))
			else:
				return HttpResponseRedirect(reverse('users'))

	return render(request, 'complaints/add_user.html', {'form': user_form})