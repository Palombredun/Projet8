from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html', {})

def legale_notice(request):
	return rend(request, 'core/legale_notice.html')