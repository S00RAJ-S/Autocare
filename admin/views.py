from django.shortcuts import redirect, render

def index(request):
    try:
        if request.session['e'] and request.session['p'] != '':
            if request.session['t'] ==  'a':
                return render(request,'adminindex.html')
            else:
                return redirect('/')
    except: 
        return redirect('/')