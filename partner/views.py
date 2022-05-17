import time
from django.shortcuts import render,redirect
from partner.models import partnerreg,partneroffer,order
from login.models import login
from user.models import bookings
from django.contrib import messages


def index(request):
    return render(request,'partnerreg.html')

def home(request):
    try:
        if request.session['e'] and request.session['p'] != '':
            if request.session['t'] == 'p':
                em = request.session['e']
                na = partnerreg.objects.get(email=em).oname
                b = bookings.objects.filter(status='b')
                return render(request,'partnerindex.html',{"name":na,'b':b})
            else:
                return redirect('/')
    except: 
        return redirect('/')
    
def submit(request):
    if request.method == 'POST':
        sn = request.POST.get('sname')
        on = request.POST.get('oname')        
        e = request.POST.get('email')
        p = request.POST.get('phone')
        ad = request.POST.get('address')
        lic = request.POST.get('license')
        paswd = request.POST.get('password')
        try:
            login.objects.get(email=e).email
            messages.warning(request, 'Email Already Exist|Try Again')
            return redirect('/partner/')
        except:
            for i in range(2,500):
                try:
                    login.objects.get(id = i).id
                    continue
                except:
                    login(id=i,email=e,password=paswd,status='pending',type='p').save()
                    partnerreg(pid_id=login.objects.get(email=e).id,sname=sn,oname=on,email=e,phone=p,address=ad,license=lic).save()
                    messages.success(request, 'Registered Your Shop Successfully|Now Login')
                    time.sleep(1)
                    return redirect('/')

def placeoffer(request):
    if request.method == "POST":
        bid = request.POST.get('bid')
        return render(request,'placeoffer.html',{'bid':bid})

def submitoffer(request):
    if request.method == "POST":
        bid = request.POST.get('bid')
        pid = request.session['id']
        wname = request.POST.get('wname')
        wphone = request.POST.get('wphone')
        rate = request.POST.get('rate')
        partneroffer(bid=bid,pid=pid,wname=wname,wphone=wphone,rate=rate).save()
        messages.success(request, 'Offer Placed Successfully')
        return redirect('/partner/bids/')

def bids(request):
    id = request.session['id']
    bids = partneroffer.objects.filter(pid=id)
    return render(request,'bids.html',{'b':bids})

def partnerorder(request):
    if request.method == "POST":
        bid = request.POST.get('bid')
        famt = request.POST.get('famt')
        order.objects.filter(bid = bid).update(finalamt=famt)
        messages.success(request,'Updated Successfully')
        return redirect('/partner/partnerorders/')
    else:
        pid = request.session['id']
        odat = order.objects.filter(pid=pid)
        return render(request,'partnerorder.html',{'odat':odat})
    
# def viewbookingpartner(request):
#     po = partneroffer.objects.all()
#     id = request.session['id']
#     ubdat ={'ub':po,'id':id}
#     try:
#         if request.session['e'] and request.session['p'] != '':
#             if request.session['t'] ==  'p':
#                 return render(request,'viewbookingpartner.html',ubdat)
#             else:
#                 return redirect('/')
#     except: 
#         return redirect('/')   