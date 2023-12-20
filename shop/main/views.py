from django.shortcuts import render,redirect

from items.models import Category,Item

from cryptography.fernet import Fernet
import base64
import logging
import traceback
# from shop.settings import key_encrypt
from django.conf import settings
from shop.settings import encrkey
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .forms import FuncSignup
from django.contrib.auth import authenticate
from django.shortcuts import render
from .models import User_Custom
from otpp.forms import MFAForm
from otpp.models import Code
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()

    return render(request,'main/index.html',
                  {'categories':categories,
                  'items':items,
                  })
    
def contact(request):
    return render(request,'main/contact.html')
#Function for encryption
def func_encrypt(passw):
    try:        
        passw = str(passw)
        # Create a Fernet object with the encryption key
        passw_ciph = Fernet(encrkey)
        # Encrypt the password using the Fernet object
        encrypt_passw = passw_ciph.encrypt(passw.encode('ascii'))
        # Convert the encrypted password to a URL-safe string
        encrypt_passw = base64.urlsafe_b64encode(encrypt_passw).decode("ascii")
        #return the encrypted password 
        return encrypt_passw
    except Exception as e:
        #log error message with traceback
        logging.getLogger("log error message").error(traceback.format_exc())
        return None
#Function for decryption
   
# def func_decrypt(passw):
#     try:
#         # Decode the URL-safe base64-encoded password
#         passw = base64.urlsafe_b64decode(passw)
#         # Create a Fernet object with the encryption key
#         passw_ciph = Fernet(settings.key_encrypt)
#         # Decrypt the password using the Fernet object
#         decod_passw = passw_ciph.decrypt(passw).decode("ascii")   
#         #return the decoded password  
#         return decod_passw
#     except Exception as e:
#         #log error message with traceback
#         logging.getLogger("log error message").error(traceback.format_exc())
#         return None  



def signup(request):
    
    if request.method=='POST':
        form=FuncSignup(request.POST)
        #check if form is valid
        if form.is_valid():
            print("Password before encryption:", form.cleaned_data['password1'])

            # Encrypt the password
            encrypted_password = func_encrypt(form.cleaned_data['password1'])
           
            # Print or log the encrypted password
            print("Encrypted Password:", encrypted_password)

            # Save the user object with the encrypted password
            new_user = form.save(commit=False)
         
            User_Custom.objects.create_user(username=new_user.username, password=encrypted_password)

            return redirect('/newlogin/')
    else:

        form=FuncSignup()

    return render(request,'main/signup.html',
        {
             'form':form
            
        })

#redirect to home page after logging out
def viewlogout(request):
    logout(request)
    return redirect('/')  


#does login
def otp_view(request):
    for user in User_Custom.objects.all():
       pass
    #    print(user.username)
    form=AuthenticationForm()
    if request.method=='POST':
        #get username
        username=request.POST.get('username')
        #get password
        passw=request.POST.get('password')
        print("usernamr",username)
        print("password",passw)
        
       
       
        if user is not None:
            request.session['pk']=user.pk
            
            return redirect('/verify/')
        else:
            print("not working")
      
        
    return render(request,'main/authent.html',{'form':form})

def verification(request):
    form=MFAForm(request.POST or None)
    #get users primary key from session data
    pk=request.session.get('pk')
    #if pk exists
    if pk:
        #get the user from the user_custom table in database
        user=User_Custom.objects.get(pk=pk)
        
        #get mfa code
        cd=user.code 
        #concatenate user name and mfa code
        cd_user=f"{user.username}:{user.code}"
        if not request.POST:
             #send the sms
            print(cd_user)
        #check if form is valid
        if form.is_valid():
            no=form.cleaned_data.get('number')
            if str(cd)==no:
                cd.save()
                login(request,user)
                return redirect('/')
            else:
                return redirect('/newlogin/')
            
    return render(request,'main/verify.html',{'form':form})



