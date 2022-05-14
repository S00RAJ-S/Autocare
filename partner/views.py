import time
from django.shortcuts import render,redirect
from partner.models import partnerreg
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
                b = bookings.objects.all()
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