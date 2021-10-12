from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
@login_required
def home(request):
    user_logged = User.get_username
    return render(request, 'base/home.html', {'user_logged': user_logged})
