from django import forms 
from django.contrib.auth.models import User
from complaints.models import Complaint, Office, Category, Platform

class ComplaintForm(forms.ModelForm):
	number = forms.CharField(label='Complaint Id', widget=forms.TextInput(attrs={'class':'form-control'}))
	message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class':'form-control'}))
	date_received = forms.DateTimeField(label='Date Received', widget=forms.TextInput(attrs={'class':'form-control'}))
	office_referred = forms.ModelChoiceField(Office.objects.all(), label='Office Referred', widget=forms.Select(attrs={'class':'form-control'}))
	sender_name = forms.CharField(label='Sender Name', widget=forms.TextInput(attrs={'class':'form-control'}))
	sender_email = forms.EmailField(label='Sender Email', widget=forms.TextInput(attrs={'class':'form-control'}))
	sender_contact = forms.CharField(label='Sender Contact #', widget=forms.TextInput(attrs={'class':'form-control'}))
	sender_company = forms.CharField(label='Sender Company', widget=forms.TextInput(attrs={'class':'form-control'}))
	# action_taken = forms.CharField()
	# date_action = forms.DateTimeField()
	# remarks = forms.CharField()
	category = forms.ModelChoiceField(Category.objects.all(), label='Category', widget=forms.Select(attrs={'class':'form-control'}))
	platform = forms.ModelChoiceField(Platform.objects.all(), label='Platform', widget=forms.Select(attrs={'class':'form-control'}))
	done = forms.BooleanField(label='Done')

	class Meta:
		model = Complaint
		exclude = ('action_taken', 'date_action', 'remarks')
		# fields = ('')