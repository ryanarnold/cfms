from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def reports(request):
	return render(request, 'reports/reports.html', {})

def monthly_detail(request, report_type):
	return HttpResponseRedirect(reverse('reports'))