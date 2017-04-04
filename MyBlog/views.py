from django.shortcuts import render
from models import Images
# Create your views here.
from rest_framework.decorators import api_view



def home(request):
    try:
        img = Images()
        var = [10,12,13,22]
        context ={'Hello':var}
        template = 'home.html'
        img.imageName = "photo.png"
        img.save()
    except Exception as ex:
        print(ex.message)
    return render(request,template,context)


def formpage(request):
    try:
        img = Images()
        print "formpage function"
        var = "Deepak"

        context ={'title':var}
        template = 'formpage.html'
        img.imageName = "photo.png"
        img.save()
    except Exception as ex:
        print(ex.message)
    return render(request,template,context)