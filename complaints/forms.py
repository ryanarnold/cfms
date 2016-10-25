from django import forms 
from django.contrib.auth.models import User
from complaints.models import Complaint

class ComplaintForm(forms.ModelForm):
	number = forms.CharField()
	message = forms.CharField()
	date_received = forms.DateTimeField()
	office_referred = forms.ModelChoiceField()
	sender_name = forms.CharField()
	sender_email = forms.EmailField()
	sender_contact = forms.CharField()
	sender_company = forms.CharField()
	action_taken = forms.CharField()
	date_action = forms.DateTimeField()
	remarks = forms.CharField()
	category = forms.ModelChoiceField()
	platform = forms.ModelChoiceField()
	done = models.BooleanField()

	class Meta:
		model = Complaint
		# fields = ('')