from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    # return HttpResponse('Teste Home')
    return render(request, 'home.html')

