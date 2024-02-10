from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, PersonalDetailForm
from users.models import User

def register_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        personal_detail_form = PersonalDetailForm(request.POST)
        print(f"\n\n User form: {user_form.is_valid()} Personal detail form: {personal_detail_form.is_valid()} \n\n")
        if user_form.is_valid() and personal_detail_form.is_valid():
            user = user_form.save()
            my_user = User.objects.get(phone=user.phone)

            if my_user is None:
                return HttpResponse("<h1>User not found</h1>")

            personal_detail = personal_detail_form.save(commit=False)
            personal_detail.user = my_user
            personal_detail.save()
            return HttpResponse("<h1>User created successfully</h1>")
        print(user_form.cleaned_data)
    else:
        user_form = UserForm()
        personal_detail_form = PersonalDetailForm()
    return render(request, 'app/registration/register.html', {'user_form': user_form, 'personal_detail_form': personal_detail_form})

def login_user(request):
    error = None
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        if phone and password:
            user = authenticate(phone=phone, password=password)
            if user is not None:
                return HttpResponse("<h1>User logged in successfully</h1>")
                # login(request, user)
            error = "Incorrect phone number or password "
        else:
            error = "Phone or password cannot be empty"

    return render(request, 'app/registration/login.html', {'error': error})

def logout_user(request):
    logout(request)
    return redirect('/')

def changePassword(request):
    return render(request, 'app/registration/changePassword.html')

def address(request):
    return render(request, 'app/registration/address.html')

def bankDetail(request):
    return render(request, 'app/registration/bank.html')
