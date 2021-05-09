from django.shortcuts import render
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.files.storage import default_storage
import random,time
from fileenc_openssl import stretch_key, encrypt_file as ef_ssl, decrypt_file as df_ssl
import base64, os
from .algorithms import encrypt,decrypt,mono_algorithms,poly_algorithms
from general_methods import utils
import re
from django.core.mail import send_mail
from .models import Key


# Create your views here.
# Create your views here.
def signin(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username=request.POST.get("username")
        psw =request.POST.get("pass")
        user = authenticate(request, username=username, password=psw)
        if user is not None:
            login(request, user)
            return redirect('index')
        
        else:
            e = "Invalid username/password."
            return render(request,'app/login.html',{'e':e})

    return render(request,'app/login.html')

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('errorpage')

    context = {
       
    }
    return render(request,'app/index.html',context)

def errorpage(request):
    return render(request,'app/errorpage.html')

def encrypt_file(request):
    if not request.user.is_authenticated:
        return redirect('errorpage')

    if request.method == 'POST':
        filename =request.FILES['file']
        f_type = os.path.splitext(str(filename))[1]
        print(f_type)
        p = '/Users/himalisaini/Desktop/css/app/static/app/assets/images/' + filename.name
        path = default_storage.save(p,filename)
        time.sleep(3)
        print(path)
        mykey = str(request.user.id) + str(request.user.username)
        enc_pth = encrypt.encrypt_fun(p,mykey)
        time.sleep(3)
        '''
        stretched_key = stretch_key(mykey)
        enc_pth = ef_ssl(new_path, key=stretched_key)
        print(enc_pth)'''
        name = f_type + '.enc'
        context = {
            'path' : 'app/assets/images/'+ str(filename.name) + '.enc' ,
            'enc' : 1,
        }
        messages.success(request, 'Encryption Successful')
        return render(request,'app/encrypt_file.html',context)


    return render(request,'app/encrypt_file.html')

def decrypt_file(request):
    if not request.user.is_authenticated:
        return redirect('errorpage')

    if request.method == 'POST':
        filename =request.FILES['file']
        print(filename.name)
        f_type = os.path.splitext(str(filename))[0]
        p = '/Users/himalisaini/Desktop/css/app/static/app/assets/images/' + filename.name
        path = default_storage.save(p,filename)
        time.sleep(3)
        print(path)
        #mykey = str(request.user.id) + str(request.user.username)
        #print(mykey)
        #stretched_key = stretch_key(mykey)
        mykey = str(request.user.id) + str(request.user.username)
        dec_path = decrypt.decrypt_fun(path,mykey)
        time.sleep(3)
        context = {
            'path' : 'app/assets/images/'+ str(f_type) ,
            'enc' : 1,
        }
        messages.success(request, 'Decryption Successful')
        return render(request,'app/decrypt_file.html',context)


    return render(request,'app/decrypt_file.html')

'''
Uses aes-256-cbc for file encryption (as implemented by openssl)
Uses a salt when encrypting (to avoid pre-computation or rainbow tables).
Uses sha256 key stretching (with <0.1s) to make brute force prohibitively expensive.
Uses sha256 checksum to check file integrity.
'''

def hash_func(request,sha):
    if not request.user.is_authenticated:
        return redirect('errorpage')

    hashed_string = ''
    msg2 = ''
    if 'encrypt' in request.POST:
        msg = request.POST.get("enc_msg")
        if sha == 'sha256':
            hashed_string = utils.sha256(msg)
            msg2 = msg
        if sha == 'sha1':
            hashed_string = utils.sha1(msg)
            msg2 = msg
        if sha == 'sha384':
            hashed_string = utils.sha384(msg)
            msg2 = msg
        if sha == 'sha512':
            hashed_string = utils.sha512(msg)
            msg2 = msg
        if sha == 'md5':
            hashed_string = utils.md5(msg)
            msg2 = msg
        if sha == 'sha224':
            hashed_string = utils.sha224(msg)
            msg2 = msg

    context = {
            'sha' : sha,
            'hashed_string':hashed_string,
            'msg':msg2,
        }

    return render(request,'app/hash.html',context)

def mono(request):
    if not request.user.is_authenticated:
        return redirect('errorpage')

    hashed_string = ''
    msg2 = ''
    tab = 1
    if 'encrypt' in request.POST:
        msg = request.POST.get("enc_msg")
        msg = re.sub('\s+',' ',msg)
        hashed_string = mono_algorithms.encrypt_mono(msg,request.user.id+7)
        msg2 = msg

    dec_string = ''
    msg3 = ''
    if 'decrypt' in request.POST:
        msg2 = request.POST.get("dec_msg")
        msg2 = re.sub('\s+',' ',msg2)
        dec_string = mono_algorithms.decrypt_mono(msg2,request.user.id+7)
        msg3 = msg2
        tab = 2

    if 'send_email' in request.POST:
        email = request.POST.get("email")
        email = re.sub('\s+',' ',email)
        subject = f'Secret message by {request.user.username}'
        message = request.POST.get("newmsg")
        email_from = 'himali.saini@somaiya.edu'
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        messages.success(request, 'Email has been sent')
       


    context = {
            'hashed_string':hashed_string,
            'msg':msg2,
            'dec_string':dec_string,
            'msg2':msg3,
            'tab':tab
        }

    return render(request,'app/mono.html',context)

def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr

def poly(request):
    if not request.user.is_authenticated:
        return redirect('errorpage')

    hashed_string = ''
    msg2 = ''
    tab = 1
    	


    if 'encrypt' in request.POST:
        msg = request.POST.get("enc_msg")
        msg = re.sub('\s+',' ',msg)
        msg = str(msg[1:])
        msg = msg.upper()
        key_v = poly_algorithms.generateKey(msg,request.user.username)
        hashed_string = poly_algorithms.cipherText(msg,key_v)
        Key.objects.create(user=request.user,key=key_v,enc_string=hashed_string).save()
        msg2 = msg

    dec_string = ''
    msg3 = ''
    if 'decrypt' in request.POST:
        msg2 = request.POST.get("dec_msg")
        msg2 = re.sub('\s+',' ',msg2)
        msg2 = str(msg2[1:])
        msgv = ''
        for x in msg2:
            if x == ' ':
                break
            msgv += x

        print(len(msg2))
        print(len(msgv))
        ob = Key.objects.get(enc_string=msgv)
        key_v = ob.key
        dec_string = poly_algorithms.originalText(msgv, key_v)
        msg3 = msgv
        tab = 2

    if 'send_email' in request.POST:
        email = request.POST.get("email")
        email = re.sub('\s+',' ',email)
        subject = f'Secret message by {request.user.username}'
        message = request.POST.get("newmsg")
        email_from = 'himali.saini@somaiya.edu'
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        messages.success(request, 'Email has been sent')
       


    context = {
            'hashed_string':hashed_string,
            'msg':msg2,
            'dec_string':dec_string,
            'msg2':msg3,
            'tab':tab
        }

    return render(request,'app/poly.html',context)