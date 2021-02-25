from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Datauser, Cities
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    """Render login page google+"""
    return render(request, 'main/main.html')


def log_out(request):
    """logout, return to login page"""
    logout(request)
    return redirect('/')


@login_required
def data(request):
    """Render info/edit page about user"""
    user = Datauser.objects.filter(username=request.user.username).first()
    if user == None:
        Datauser.objects.create(username=request.user.username)  # создаем нового юзера, если его не существует
    user = Datauser.objects.get(username=request.user.username)
    cities = Cities.objects.all()
    return render(request, 'main/data.html', {'user_name': request.user.username,
                                              'user_email': str(request.user.email),
                                              'user_data': user, 'cities': cities})


@login_required
def loaddata(request):
    """Uploads info about user to database"""
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
    return render(request, 'main/data.html', {'user_name': request.user.username,
                                              'user_email': str(request.user.email),
                                              'user_data': user})


@login_required
def catalog(request):
    """Show gallery with all users"""
    users_data = Datauser.objects.all()
    return render(request, 'main/catalog.html', {'users_data': users_data})
