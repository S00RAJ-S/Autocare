from django.shortcuts import render,redirect
from .models import login
def index(request):
    try:
        if request.session['e'] and request.session['p'] != '':
            if request.session['t'] == 'a':
                return redirect('/admin/')
            elif request.session['t'] == 'p':
                return render(request,'partnerindex.html')
            elif request.session['t'] == 'u':
                return render(request,'userindex.html')
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
                if i.type == 'a':
                    request.session['t'] = 'a'
                    return redirect('/admin/')
                elif i.type == 'p':
                    request.session['t'] = 'p'
                    return render(request,'partnerindex.html')
                elif i.type == 'u':
                    request.session['t'] = 'u'
                    return render(request,'userindex.html')
            else:
                continue
        return render(request,'loginerror.html')          

def logout(request):
    try:
        del request.session['e']
        del request.session['p'] 
        del request.session['t']
        return redirect('/')
    except:
        return redirect('/')
