from django.shortcuts import render,redirect
from .models import login
from django.contrib import messages

def index(request):
    try:
        if request.session['e'] and request.session['p'] != '':
            if request.session['t'] == 'a':
                return redirect('/admin/')
            elif request.session['t'] == 'p':
                return redirect('/partner/home/')
            elif request.session['t'] == 'u':
                return redirect('/user/home/')
    except:
        return render(request,'login.html')

def submit(request):
    if request.method == 'POST':
        e = request.POST.get('email')
        p = request.POST.get('password')
        d = login.objects.all()
        for i in d :
            if i.email == e and i.password == p:
                request.session['e'] = e
                request.session['p'] = p
                request.session['id'] = i.id
                if i.type == 'a':
                    request.session['t'] = 'a'
                    return redirect('/admin/')
                elif i.type == 'p':
                    request.session['t'] = 'p'
                    return redirect('/partner/home/')
                elif i.type == 'u':
                    request.session['t'] = 'u'
                    return redirect('/user/home/')
            else:
                continue
        messages.warning(request,"Invalid Credentials|Please Try again")
        return redirect('/')          

def logout(request):
    try:
        del request.session['e']
        del request.session['p'] 
        del request.session['t']
        return redirect('/')
    except:
        return redirect('/')
