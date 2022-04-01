from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'registration.html')

def submit(request):
    if request.method == 'POST':
        n = request.POST.get('name')
        e = request.POST.get('email')
        p = request.POST.get('phone')
        ad = request.POST.get('address')
        paswd = request.POST.get('password')
        return HttpResponse('Yes working')
