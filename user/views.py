import email
from django.contrib import messages
from django.shortcuts import render,redirect
from user.models import userreg
from login.models import login

def index(request):
    return render(request,'registration.html')

def home(request):
    try:
        if request.session['e'] and request.session['p'] != '':
            if request.session['t'] == 'u':
                em = request.session['e']
                na = userreg.objects.get(email=em).name
                return render(request,'userindex.html',{"name":na})
            else:
                return redirect('/')
    except: 
        return redirect('/')

def submit(request):
    if request.method == 'POST':
        n = request.POST.get('name')
        e = request.POST.get('email')
        p = request.POST.get('phone')
        ad = request.POST.get('address')
        paswd = request.POST.get('password')
        try:
            login.objects.get(email=e).email
            messages.warning(request, 'Email Already Exist|Try Again')
            return redirect('/user/')
        except:
            for i in range(500,10000):
                try:
                    login.objects.get(id = i).id
                    continue
                except:
                    login(id=i,email=e,password=paswd,status='approved',type='u').save()
                    userreg(uid_id=login.objects.get(email=e).id,name=n,email=e,phone=p,address=ad).save()
                    messages.success(request, 'Registered Successfully|Now Login')
                    return redirect('/')
