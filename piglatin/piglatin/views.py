#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def translate(request):
    original = request.GET['originaltext'].lower()
    translated = []
    
    for word in original.split():
        if word[0] in 'aeiou': # vowel
            translated.append(word+'yay')
        else:# consonant
            translated.append(word[1:]+word[0]+'ay')
    
    translatedStr = ' '.join(translated)
    #return HttpResponse(' '.join(translated))
    return render(request, 'translate.html',\
                  {'original':original, \
                   'translated':translatedStr})

def about(request):
    return render(request, 'about.html')