from django.shortcuts import render , redirect
from .models import Profile
import random 
import http.client

def send_otp(mobile,otp):
    conn = http.client.HTTPSConnection("api.msg91.com")
    authkey = '415865Ar1BMruE65c8fa07P1'
    
    headers = {'content-type':"appliction/json"}
    url = "http://control.msg91.com/api/sendotp.php?otp="+otp+ "&sender=a23&message="+"your otp is " +otp + "&mobile="+ mobile+"&authkey="+authkey+"&country=91"
    url = url.replace(" ", "%20")
    # url = "http://control.msg91.com/api/sendotp.php?otp="+otp+ "&sender=ABC&message="+"your otp is " + otp + "&mobile="+ mobile+"&authkey="+authkey+"&country=91"
    #url = "http://control.msg91.com/api/sendotp.php?otp=" + otp + "&sender=ABC&message=your%20otp%20is%20" + otp + "&mobile=" + mobile + "&authkey=" + authkey + "&country=91"
   

    conn.request("GET",url,headers=headers)
    res = conn.getresponse()
    data = res.read()
    print("otp sent done!")

    print(url)
    return None

def login_views(request):
    return render(request,"test/login.html")

def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')

        check_user = Profile.objects.filter(mobile=mobile).first()
        print(email)
        print(name)
        print(mobile)

        if check_user:
            context = {'message':'mobile already taken','class':'danger'}
            return render(request,'test/register.html',context)
        otp = str(random.randint(1000,9999))
        profile= Profile(user=name,mobile=mobile,otp=otp)
        profile.save()
        send_otp(mobile,otp)
        request.session['mobile']= mobile
        return redirect('otptest:test_register')
        redirect("userauths:signup")



    return render(request,"test/register.html")
    

def otp(request):
    mobile = request.session['mobile']
    context = {'mobile':mobile}
    return render(request,"test/otp.html",context)

# from django.shortcuts import render 
# from .models import Profile
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .helpers import send_otp_to_phone
# from .models import  user
# @api_view(['POST'])
# def send_otp(request):
#     data = request.data

#     if data.get('phone_number') is None:
#         return Response({
#             'status':400,
#             'meesage':'key phone_number is required'
#         })
    
#     if data.get('password') is None:
#         return Response({
#             'status':400,
#             'meesage':'key password is required'
#         })
    

#     User = user.objects.create(
#         phone_number = data.get('phone_number'),
#         otp = send_otp_to_phone(data.get('phone_number'))
#         )
#     user.save()

#     return Response({
#         'status':200,'message':'otp Sent'
#     })
