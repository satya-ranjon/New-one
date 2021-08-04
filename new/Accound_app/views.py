from django.contrib.messages.api import success
from django.shortcuts import redirect, render,HttpResponseRedirect
from django.urls import reverse
from .forms import Login_user,sign_user,Change_password
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login,get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# email send email veryfy
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, message, send_mail
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
UserModel = get_user_model()
# Create your views here.




def signup_user(request):
    form = sign_user()
    if request.method == 'POST':
        form = sign_user(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate Your accound'
            message = render_to_string('Accound_app/send.html', context={
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            send_mail = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[send_mail])
            email.send()
            messages.success(request, 'You have Successfully Sign up here ! Please @Login')
            messages.info(request, 'Your Accound do not active chak your email  ')
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'Accound_app/sign.html',{'title':'Sign up','form':form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(
            request, 'Your Accound is activated noe you can login now ')
        return HttpResponseRedirect(reverse('login'))
    else:
        messages.warning(request, 'Active link is invalid')
        return HttpResponseRedirect(reverse, ('sign'))


def login_user(request):
    form = Login_user()
    if request.method == 'POST':
        form = Login_user(data=request.POST,request=request)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'You have successfully login')
                return HttpResponseRedirect(reverse('home'))
            messages.info(request,'User ')
            return HttpResponseRedirect(reverse('login'))
        messages.error(request,'User name and password not valid ')
        return HttpResponseRedirect(reverse('login'))

    return render(request, 'Accound_app/login.html',{'title':'login ','form':form})

@login_required()
def logout_user(request):
    logout(request)
    messages.success(request,'You have successfully logout ! Please @login agin')
    return HttpResponseRedirect(reverse('home'))


@login_required()
def change_password(request):
    form = Change_password(request.user)
    if request.method == 'POST':
        form = Change_password(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,' Your Password successfully change !')
            return HttpResponseRedirect(reverse('login'))
    return render(request,'Accound_app/change_password.html',{'form':form})





