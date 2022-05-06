from django.contrib import messages
from django.shortcuts import render,redirect
from user.models import userreg,bookings
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

def submitbooking(request):
    if request.method == 'POST':
        details = request.POST.get('details')
        category = request.POST.get('category')
        userid = request.session['id']
        for i in range(1,10000):
                try:
                    bookings.objects.get(id = i).bid
                    continue
                except:
                    bookings(bid=i,uid=userid,details=details,category=category).save()
                    messages.success(request, 'Your Booking has been received')
                    return redirect('/')
                
def mybookings(request):
    uid = request.session['id']
    ub = bookings.objects.all()
    ubdat ={'ub':ub,'uid':uid}
    try:
        if request.session['e'] and request.session['p'] != '':
            if request.session['t'] ==  'u':
                return render(request,'viewbookinguser.html',ubdat)
            else:
                return redirect('/')
    except: 
        return redirect('/')   

def delbooking(request):
    if request.method == 'POST':
        bookingid = request.POST.get('bid')
        try:
            bookings.objects.filter(bid=bookingid).delete()
            # partneroffer.objects.filter(bid=bookingid).delete()
            messages.success(request,'Successfully Deleted Your Booking')
            return redirect('/user/mybookings/')
        except:
            messages.warning(request,'Not Deleted')
            return redirect('/user/mybookings/')