from django import forms 
from django.contrib.auth.models import User
from complaints.models import Complaint, Office, Category, Platform

class ComplaintForm(forms.ModelForm):
	number = forms.CharField(label='Complaint Id', widget=forms.TextInput(attrs={'class':'form-control'}))
	message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class':'form-control'}))
	# date_received = forms.DateTimeField(label='Date Received', widget=forms.DateTimeInput(attrs={'class':'form-control'}))
	category = forms.ModelChoiceField(Category.objects.all(), label='Category', widget=forms.Select(attrs={'class':'form-control'}))
	platform = forms.ModelChoiceField(Platform.objects.all(), label='Platform', widget=forms.Select(attrs={'class':'form-control'}))
	office_referred = forms.ModelChoiceField(Office.objects.all(), label='Office Referred', widget=forms.Select(attrs={'class':'form-control'}))
	sender_name = forms.CharField(label='Sender Name', widget=forms.TextInput(attrs={'class':'form-control'}))
	sender_email = forms.EmailField(label='Sender Email', widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
	sender_contact = forms.CharField(label='Sender Contact #', widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
	sender_company = forms.CharField(label='Sender Company', widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
	# action_taken = forms.CharField()
	# date_action = forms.DateTimeField()
	# remarks = forms.CharField()
	# done = forms.BooleanField(label='Done', widget=forms.CheckboxInput(attrs={'class':'form-control'}))

	class Meta:
		model = Complaint
		fields = ('number', 
			'message', 
			'category', 
			'platform', 
			'office_referred', 
			'sender_name', 
			'sender_email', 
			'sender_contact', 
			'sender_company')
		exclude = ('action_taken', 'date_action', 'remarks', 'done', 'date_received')

class UpdateComplaintForm(ComplaintForm):
	action_taken = forms.CharField(label='Action Taken', widget=forms.Textarea(attrs={'class':'form-control'}), required=False)
	date_action = forms.DateTimeField(label='Date of Action', widget=forms.DateTimeInput(attrs={'class':'form-control datetime-picker'}), required=False)
	remarks = forms.CharField(label='Remarks', widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
	done = forms.BooleanField(label='Done', widget=forms.CheckboxInput(attrs={'class':'form-control'}), required=False)

	class Meta:
		model = Complaint
		fields = ('number', 
			'message', 
			'category', 
			'platform', 
			'office_referred', 
			'sender_name', 
			'sender_email', 
			'sender_contact', 
			'sender_company',
			'action_taken', 
			'done',
			'date_action', 
			'remarks')

class UserForm(forms.ModelForm):
	username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ('first_name', 
			'last_name',
			'username', 
			'password')

class PlatformForm(forms.ModelForm):
	name = forms.CharField(label='Platform Name', widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Platform
		fields = ('name',)

class CategoryForm(forms.ModelForm):
	name = forms.CharField(label='Category Name', widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Category
		fields = ('name',)

class OfficeForm(forms.ModelForm):
	name = forms.CharField(label='Office Name', widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = Office
		fields = ('name',)