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
                    if i.status == 'approved':
                        request.session['t'] = 'p'
                        return redirect('/partner/home/')
                    else:
                        messages.warning(request,"Your Partner Request not approved|Please Try Later or contact admin")
                        return redirect('/')
                elif i.type == 'u':
                    request.session['t'] = 'u'
                    return redirect('/user/home/')
            else:
                continue
        messages.warning(request,"Invalid Credientials or not registered|Please Try Again")
        return redirect('/')          

def logout(request):
    try:
        del request.session['e']
        del request.session['p'] 
        del request.session['t']
        return redirect('/')
    except:
        return redirect('/')
