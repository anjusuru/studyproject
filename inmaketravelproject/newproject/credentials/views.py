from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Authentication Failed")
            return redirect('login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request,'/index')

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken!")
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist!")
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password)

                user.save()
                messages.success(request, "Profile created")
                return redirect('login')
        else:
            messages.info(request, "password does not match")
            return redirect('registration')

        return redirect('registration')
    return render(request, 'registration.html')
