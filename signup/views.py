from django.shortcuts import render


#def signup():
#    pass
def signup(request):
    return render(request, 'signup/signup.html', {})