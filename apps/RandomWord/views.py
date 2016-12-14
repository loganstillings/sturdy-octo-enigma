from django.shortcuts import render, HttpResponse, redirect
import random
import string
# Create your views here.
def index(request):
    if 'num' not in request.session:
        request.session['num'] = 0
    return render(request, "RandomWord/index.html")

def create(request):
    if request.method == "POST":
        request.session['num'] += 1
        request.session['random_word'] = ''.join([random.choice(string.ascii_uppercase + string.digits) for n in xrange(14)])
        return redirect('/')
    else:
        return redirect('/')

def reset(request):
    if 'random_word' in request.session:
        del request.session['num']
        del request.session['random_word']
    return redirect('/')
