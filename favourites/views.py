from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#from profiles.models import UserProfile

@login_required
def favourites(request):
	current_user = {'user': request.user}
	return render(request, 'favourites/favourites.html', current_user)