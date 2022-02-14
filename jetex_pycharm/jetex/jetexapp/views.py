from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import RentForm, HireForm
from .models import ProfessionList, Contactus

def thankyou(request):
    return render(request, 'thankyou.html')

def Home(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('wgtmsr') and request.POST.get('message'):
            saverecord = Contactus()
            saverecord.name = request.POST.get('name')
            saverecord.email = request.POST.get('email')
            saverecord.subject = request.POST.get('wgtmsr')
            saverecord.message = request.POST.get('message')
            saverecord.save()
            return redirect("/")
        else:
            messages.info(request, "please enter again.. you did something wrong...")
            return redirect ('/')
    else:
        return render(request, 'index.html')


def Insertrecord(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('profession') and request.POST.get('birthday') and request.POST.get('gender') and request.POST.get('phone') and request.POST.get('city') and request.POST.get('pincode'):
            saverecord = ProfessionList()
            saverecord.name = request.POST.get('name')
            saverecord.email = request.POST.get('email')
            saverecord.profession = request.POST.get('profession')
            saverecord.birthday = request.POST.get('birthday')
            if request.POST.get('gender') == 'on':
                saverecord.gender = 'Male'
            else:
                saverecord.gender = 'Female'
            saverecord.phone = request.POST.get('phone')
            saverecord.city = request.POST.get('city')
            saverecord.pincode = request.POST.get('pincode')
            saverecord.save()
            messages.success(request, 'record saved successfully....!')
            return redirect("/")
            
        else:
            messages.info(request, "please enter again.. you did something wrong...")
            return redirect ('professionregister')

    else:
        return render(request, 'professionregister.html')




def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "username or password wrong")
            return redirect('login')

    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        user_name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']
        
        if password == re_password:
             
            if User.objects.filter(email = email).exists():
                messages.info(request, "you are already have account click on login")
                return redirect('register')

            else:
                user = User.objects.create_user(username = user_name, email = email, password = password)
                user.save()
                messages.info(request, "account successfully created")
                return redirect('login') 
        else:
            messages.info(request, "passwords not matching")
            return redirect('register')

    else:
        return render(request, 'register.html')

       

    

def rent(request):
    form = RentForm()
    submitted = False
    if request.method == 'POST':
        print(request.POST)
        form = RentForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    
    return render(request, 'rent.html', {'form':form})   

def hire(request):
    form = HireForm()
    submitted = False
    if request.method == 'POST':
        print(request.POST)
        form = HireForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    
    return render(request, 'hire.html', {'form':form})

 

def logout(request):
    auth.logout(request)
    return redirect('/')
