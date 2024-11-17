#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("Hello word I m home.")
    return render(request, 'home.html')
  
  
def about(request):
    # return HttpResponse("I am About Page")
    return render(request, "about.html")