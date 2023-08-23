from django.contrib.auth.models import User
from django.shortcuts import render


def homepage(request):
    users = User.objects.all()
    return render(request, 'main/mainpage.html')


def users_in_db(request):
    users = User.objects.all()
    users = users.values()
    return render(request, 'main/users.html', {'users': users})
