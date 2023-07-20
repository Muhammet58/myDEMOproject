from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_request(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST["login_username"]
        password = request.POST["login_password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'account/login.html', {"error":"Kullanıcı adınızı yada parola bilginizi yanlış girdiniz !"})

    return render(request, 'account/login.html', )
5
def register_request(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST["register_username"]
        password = request.POST["register_password"]
        re_password = request.POST["register_re-password"]
        email = request.POST["register_email"]
        firstname = request.POST["register_name"]
        lastname = request.POST["register_surname"]

        if password == re_password:
            if User.objects.filter(username=username).exists():
                return render(request, 'account/register.html', {'error': 'Bu kullanıcı adı başkası tarafından kullanılıyor !',
                                                                 'email': email,
                                                                 'username': username,
                                                                 'name': firstname,
                                                                 'surname': lastname})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, 'account/register.html',{'error': 'Bu e-posta adresi başkası tarafından kullanılıyor !',
                                                                    'email': email,
                                                                    'username': username,
                                                                    'name': firstname,
                                                                    'surname': lastname})
                else:
                    user = User.objects.create_user(username=username, email=email, first_name=firstname, last_name=lastname, password=password)
                    user.save()
                    return redirect("login_url")

        else:
            return render(request, 'account/register.html', {'error':'Parola bilgileri eşleşmiyor !',
                                                             'email': email,
                                                             'username': username,
                                                             'name': firstname,
                                                             'surname': lastname
                                                             })

    return render(request, 'account/register.html',)

def logout_request(request):
    logout(request)
    return redirect("/")