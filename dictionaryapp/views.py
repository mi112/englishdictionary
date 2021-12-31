from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.


def index(request):
    return render(request, "index.html")


def word(request):

    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    #synonyms = dictionary.synonym(search)
    #antonyms = dictionary.antonym(search)
    '''if not meaning:
        meaning = {'No results found':['Please try another word']}
'''
    context = {
        'word':search,
        'meaning': meaning,
        #'synonyms': synonyms,
        #'antonyms': antonyms
    }
    return render(request, 'word.html', context)