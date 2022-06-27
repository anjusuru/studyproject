from django.shortcuts import render
from django.http import HttpResponse
from .models import Place,Destination
# Create your views here.
def demo(request):
 # return HttpResponse("hello world")
  return render(request,'home.html')
def index(request):
    obj=Place.objects.all()
    obj1=Destination.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})