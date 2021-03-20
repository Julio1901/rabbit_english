from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import WordForm
from django.conf import settings
from django.shortcuts import redirect

def insertWord(request):
    #check if user is logged in, if not, redirect to login screen
    if not request.user.is_authenticated:
        return redirect('/authenticate/user-login')
    else:
        if request.method == 'POST':
            form = WordForm(request.POST)
            if form.is_valid():
                return HttpResponseRedirect('add-word')
            else:
                return HttpResponseRedirect('add-word')
        else:
            form = WordForm()
            return render(request, 'word_form.html', {'form': form})

