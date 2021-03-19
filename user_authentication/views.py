from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import *

# Create your views here.

def testView(request):
    return render(request, 'test.html')

def createTest(request):

    #user =  User.objects.create_user('leko', 'leko@gmail.com', 'teste@123')
    #user.last_name = 'Santos'
    #user.save()

    if request.method == 'POST':
        form = registrationForm(request.POST)
        
        email = 'test'
        if form.is_valid():
            return render(request, 'create.html', {'email':email})
    else:
        form = registrationForm()
        return render(request, 'create_user.html', {'form':form})
        


    #return render(request, 'create.html', {'name':name})
