from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def firstView(request):
    return HttpResponse('This is my first view')
def ViewWithTag(request):
    return HttpResponse('<h1>I had created a view using Tag<h1>')
def viewMultipleTags(request):
    return HttpResponse('<h1><marquee>view with multiple tags</marquee></h1>')
def BioData(request):
    return HttpResponse('''<h1>I am Anjali</h1>
                        <h1><i>i am 21 yeas old</i><h1>
                        <h1><b> i am from andhraPradesh</b></h1>
                        <img src="">''')
    

