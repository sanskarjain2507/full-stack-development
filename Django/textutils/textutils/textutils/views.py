#i have created this file
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse("helloworld")
#
#
# def about(request):
#     return HttpResponse("about window")
params={'name':'sanskar' , 'place':'india'}
def index(request):
    return render(request,'index.html',params)

def removepunc(request):
    djtext1=request.GET.get('ta1','default') #get the text
    print(djtext1)
    return HttpResponse("remove punc <a href='/'>back<a>")

def capfirst(request):
    return HttpResponse("capatilize first <a href='/'>back<a>")

def newlineremove(request):
    return HttpResponse("new line remover <a href='/'>back<a>")

def spaceremove(request):
    return HttpResponse("spaceremove <a href='/'>back<a>")

def charcount(request):
    return HttpResponse("charcount <a href='/'>back<a>")


def analyze(request):
    djtext1 = request.POST.get('ta1', 'default')
    chk1 = request.POST.get('removepunc', 'off')
    fullcap=request.POST.get('fullcaps','off')
    newliner = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')

    if chk1=='on':
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext1:
            if char not in punctuations:
                  analyzed+=char

        print(chk1)
        params={'purpose':'remove punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif fullcap=='on':
        djtext2=djtext1.upper()
        return render(request,'analyze.html',{'capital':djtext2})
    elif newliner=='on':
        analyzed=""
        for char in djtext1:
            if char!='\n' and char!='\r':
                analyzed+=char
        return render(request, 'analyze.html', {'newlineremovedtext': analyzed})
    elif spaceremover=='on':
        djtext2=djtext1.replace(" ",'')
        return render(request,'analyze.html',{'spacerem':djtext2})
    else:
        return HttpResponse("something wrong")
