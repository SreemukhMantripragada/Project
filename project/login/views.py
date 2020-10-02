from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def login(request):
    if request.method=="POST":
        print(request.POST.keys())
        name = request.POST['user_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['Confirm']
        usertype = bool(request.POST['user']=='Teacher')
        if password==confirm:
            if User.objects.filter(username=name).exists():
                messages.info(request, 'Username taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
            else:
                user = User.objects.create_user(username = name,email = email, password = password, is_staff = usertype)
                user.save()

        else:
            messages.info(request, 'Please enter the same password')
        #return render(request, 'home.html')
        return redirect('/')

    if request.method=='GET':
        return render(request, 'login-page.html')