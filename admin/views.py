from django.shortcuts import redirect, render

def index(request):
    try:
        if request.session['e'] and request.session['p'] != '':
            return render(request,'adminindex.html')
    except: 
        return redirect('/')