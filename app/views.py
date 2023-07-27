from django.shortcuts import render

# Create your views here.
def abc(request):
    d={'name':'siddhu','age':23}
    return render(request,'abc.html',context=d)