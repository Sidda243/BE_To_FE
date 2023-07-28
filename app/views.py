from django.shortcuts import render

# Create your views here.
def abc(request):
    d={'name':'siddhu','age':23}
    return render(request,'abc.html',context=d)

def if_else(request):
    d={'a':20,'b':40}
    return render(request,'if_else.html',context=d)

def if_elif(request):
    d={'a':20,'b':40,'c':50}
    return render(request,'if_elif.html',context=d)

def nested_if(request):
    d={'a':100}
    return render(request,'nested_if.html',context=d)