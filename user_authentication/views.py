from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import *

def testView(request):
    return render(request, 'test.html')

def createTest(request):

    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            #Get values form
            form_values = request.POST.dict()
            username = form_values.get('name')
            email = form_values.get('email')
            password = form_values.get('password')
            
            #Checks if user is already registered 
            all_users = User.objects.all()
            has_email_in_database = False
            has_user_name_in_database = False
            menssage = 'Create your login'
            for one_user in all_users:
                email_user = one_user.email
                username_check = one_user.username
                if email_user == email:
                    has_email_in_database = True
                    message = 'Email adress alredy exist'
                    break
                if username_check == username:
                    has_user_name_in_database = True
                    message = 'The username already exists. Please choose another one.'
                    break
            #Create user if it does not exist
            if has_email_in_database == False and has_user_name_in_database == False:
                user =  User.objects.create_user(f'{username}',f'{email} ',f'{password}')
                user.save()
                return render(request, 'create.html', {'teste':has_email_in_database})
            #Return to form page with message explaining error on the user create
            else:
                form = registrationForm(request.POST)
                return render(request, 'create_user.html', {'form':form,'message':message})

    else:
        form = registrationForm()
        return render(request, 'create_user.html', {'form':form})

def userLogin(request):
    if request.method == 'POST':
        form = loginForm(request.POST)

        if form.is_valid():
            #form_values = request.POST.dict()
            #email = form_values.get('email')
            #password = form_values.get('password')
            #another way to do this
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=f'{email}', password=f'{password}')

            if user is not None:
                #test login
                login(request, user)
                #return redirect('/students/add-word')
                return render (request,  'index.html')
            else:
                return render(request, 'test.html')
    else:
        form = loginForm()
        return render(request, 'user_login.html', {'form':form})

def userLogout(request):
    logout(request)
