from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import WordForm

def insertWord(request):
    if request.method == 'POST':
        
        form = WordForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('add-word')
        else:
            return HttpResponseRedirect('add-word')

    else:
        form = WordForm()
        return render(request, 'word_form.html', {'form': form})

