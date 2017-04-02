from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view


@api_view(['GET'])
def home(request):
    var = [10,12,13,22]
    context ={'Hello':var}
    template = 'home.html'
    return render(request,template,context)