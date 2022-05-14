from django.shortcuts import redirect, render
from django.contrib import messages
from login.models import login
from user.models import userreg
from partner.models import partnerreg

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

def viewusers(request):
    userdat = userreg.objects.all()
    udat ={'ud':userdat}
    try:
        if request.session['e'] and request.session['p'] != '':
            if request.session['t'] ==  'a':
                return render(request,'viewusers.html',udat)
            else:
                return redirect('/')
    except: 
        return redirect('/')

def deluser(request):
    if request.method == "POST":
        userid = request.POST.get('uid')
        try:
            login.objects.filter(id=userid).delete()
            userreg.objects.filter(uid_id=userid).delete()
            messages.success(request,'Successfully Deleted')
            return redirect('/admin/viewusers/')
        except:
            messages.warning(request,'Not Deleted')
            return redirect('/admin/viewusers/')

def viewpartners(request):
    partnerdat = partnerreg.objects.all()
    pdat ={'pd':partnerdat}
    try:
        if request.session['e'] and request.session['p'] != '':
            if request.session['t'] ==  'a':
                return render(request,'viewpartners.html',pdat)
            else:
                return redirect('/')
    except: 
        return redirect('/')

def delpartner(request):
    if request.method == "POST":
        partnerid = request.POST.get('pid')
        try:
            login.objects.filter(id=partnerid).delete()
            partnerreg.objects.filter(pid_id=partnerid).delete()
            messages.success(request,'Successfully Deleted')
            return redirect('/admin/viewpartners/')
        except:
            messages.warning(request,'Not Deleted')
            return redirect('/admin/viewpartners/')

def approvals(request):
    partnerids = login.objects.filter(type='p',status='pending')
    mylis = []
    for c in partnerids:
        mylis.append(c.id)
    partnerdat = []
    for a in mylis: 
        partnerdat.append(partnerreg.objects.get(pid_id=a))
    pdat ={'pd':partnerdat}
    try:
        if request.session['e'] and request.session['p'] != '':
            if request.session['t'] ==  'a':
                return render(request,'approvals.html',pdat)
            else:
                return redirect('/')
    except: 
        return redirect('/')

def approved(request):
    if request.method == "POST":
        pid = request.POST.get('pid')
        try:
            login.objects.filter(id=pid).update(type='p',status='approved')
            messages.success(request,'Successfully Approved')
            return redirect('/admin/approvals/')
        except:
            messages.warning(request,'Not Deleted')
            return redirect('/admin/approvals/')

def approvedp(request):
    partnerids = login.objects.filter(type='p',status='approved')
    mylis = []
    for c in partnerids:
        mylis.append(c.id)
    partnerdat = []
    for a in mylis: 
        partnerdat.append(partnerreg.objects.get(pid_id=a))
    pdat ={'pd':partnerdat}
    try:
        if request.session['e'] and request.session['p'] != '':
            if request.session['t'] ==  'a':
                return render(request,'approvedp.html',pdat)
            else:
                return redirect('/')
    except: 
        return redirect('/')    