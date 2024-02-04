from django import forms
from .models import User
from app.models import PersonalDetail, AddressDetail, BankDetail, LoanApplication

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone', 'password1', 'password2', 'otp', 'terms_accepted']

class PersonalDetailForm(forms.ModelForm):
    class Meta:
        model = PersonalDetail
        fields = ['first_name', 'last_name']

class RegistrationForm(forms.Form):
    user = UserForm()
    personal_detail = PersonalDetailForm()


# from django.shortcuts import render, redirect
# from .forms import RegistrationForm

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user_form = form.cleaned_data['user']
#             personal_detail_form = form.cleaned_data['personal_detail']

#             # Save the User instance and get the created user
#             user = user_form.save()

#             # Set the user of the PersonalDetail instance and save it
#             personal_detail = personal_detail_form.save(commit=False)
#             personal_detail.user = user
#             personal_detail.save()

#             return redirect('home')
#     else:
#         form = RegistrationForm()

#     return render(request, 'register.html', {'form': form})