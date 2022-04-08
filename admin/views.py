from django.shortcuts import redirect, render
from login.models import login

def index(request):
    tu = login.objects.filter(type='u').count()
    tp = login.objects.filter(type='p').count()
    tpa = login.objects.filter(status='approved',type='p').count()
    tpna = login.objects.filter(status='pending',type='p').count()
    dat ={'tu':tu,'tp':tp,'tpa':tpa,'tpna':tpna}
    try:
        if request.session['e'] and request.session['p'] != '':
            if request.session['t'] ==  'a':
                return render(request,'adminindex.html',dat)
            else:
                return redirect('/')
    except: 
        return redirect('/')