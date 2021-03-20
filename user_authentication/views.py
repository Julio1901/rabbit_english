from django.shortcuts import render
from django.contrib.auth.models import User
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
            
            #Checks if email is already registered 
            all_users = User.objects.all()
            has_email_in_database = False
            for one_user in all_users:
                email_user = one_user.email
                if email_user == email:
                    has_email_in_database = True
                    break
            #Create user if it does not exist
            if has_email_in_database == False:
                user =  User.objects.create_user(f'{username}',f'{email} ',f'{password}')
                user.save()
                return render(request, 'create.html', {'teste':has_email_in_database})
            else:
                form = registrationForm()
                return render(request, 'has_email_in_database.html')
    else:
        form = registrationForm()
        return render(request, 'create_user.html', {'form':form})
