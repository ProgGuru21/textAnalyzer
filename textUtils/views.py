# this file was manually created by aarya dhanani
from django.http import HttpResponse
from django.shortcuts import render

# learning code
# def index(request):
#     return HttpResponse("<h2>My name is Aarya Dhanani</h2> <a href='https://light-novelpub.com/lightnovelpub/wu-dong-qian-kun/chapter-734-demon-sound-mountain'>click</a>")
#
# def about(request):
#     return HttpResponse("<center><b>About Aarya Dhanani</b></center>")

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>Home</h1>")

def analyze(request):
    text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(fullcaps == "on"):
        analyzed = ""
        for char in text:
            analyzed += char.upper()

        params = {'purpose': 'Full uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (newlineremove == "on"):
        analyzed = ""
        for char in text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(text):
            if not (text[index] == " " and text[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error')



# def capitalizefirst(request):
#
#     return HttpResponse("capitalize")
#
# def newlineremove(request):
#
#     return HttpResponse("remove new line")
#
# def spaceremove(request):
#     return HttpResponse("Remove space")
#
# def charcount(request):
#     return HttpResponse("char counter")