from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import WordForm
from .models import *
from django.conf import settings
from django.shortcuts import redirect
from user_authentication.forms import *
from django.core.paginator import Paginator

def insertWord(request):
    #check if user is logged in, if not, redirect to login screen
    if not request.user.is_authenticated:
        return redirect('/authenticate/user-login')
    else:
        if request.method == 'POST':
            form = WordForm(request.POST)
            if form.is_valid():
                word_to_save = request.POST['word']
                translate_to_save = request.POST['translate']
                user_name_to_register = request.user
                word_with_translate = Words(user_name = f'{user_name_to_register}',word= f'{word_to_save}', translate= f'{translate_to_save}')
                word_with_translate.save()
                return HttpResponseRedirect('add-word')
            else:
                return HttpResponseRedirect('add-word')
        else:
            form = WordForm()
            return render(request, 'word_form.html', {'form': form})

def DisplayAllWords(request):
    if not request.user.is_authenticated:
        return redirect('/authenticate/user-loguin')
    else:
        all_registers_by_user = Words.objects.filter(user_name='Julio Cesar Pereira')
        #Pagination to all registers

        registers_to_display_per_page = Paginator(all_registers_by_user, 5)
        page_number = request.GET.get('page')
        page_obj = registers_to_display_per_page.get_page(page_number)

        #Check out a better way to abstract this
        all_words = []
        for x in all_registers_by_user:
            word = x.word
            translate = x.translate
            user_name = x.user_name
            all_words.append((word, translate))
        return render(request, 'display_all_words.html', {'all_words': all_words, 'user_name':user_name, 'page_obj': page_obj})
        #return render(request, 'display_all_words.html', {'page_obj' : page_obj})
