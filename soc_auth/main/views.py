from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Datauser, Cities
from django.core.files.storage import FileSystemStorage

# Create your views here.

def main(request):
    return render(request, 'main/main.html')

def log_out(request):
    logout(request)
    return redirect('/')

def data(request):
    try:
        user = Datauser.objects.get(username=request.user.username)
    except: Datauser.objects.create(username=request.user.username)
    user = Datauser.objects.get(username=request.user.username)
    cities = Cities.objects.all()
    return render(request, 'main/data.html', {'user_name': request.user.username, 'user_email': str(request.user.email), 'user_data': user, 'cities': cities})

def loaddata(request):
    user = Datauser.objects.get(username=request.user.username)
    user.fio = request.POST.get('fio')
    user.city = request.POST.get('city')
    user.info = request.POST.get('info')

    user_image = request.FILES['photo']
    fs = FileSystemStorage()
    filename = fs.save(str(request.user.username) + '.jpg', user_image)
    user.image = str(request.user.username) + '.jpg'
    user.save()
    user = Datauser.objects.get(username=request.user.username)
    return render(request, 'main/data.html', {'user_name': request.user.username, 'user_email': str(request.user.email), 'user_data': user})

def catalog(request):
    users_data = Datauser.objects.all()
    return render(request, 'main/catalog.html', {'users_data': users_data})