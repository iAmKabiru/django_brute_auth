from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
		print(ip)
	return render(request, 'brute/home.html', {})