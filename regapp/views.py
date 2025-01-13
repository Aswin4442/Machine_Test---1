from django.shortcuts import render,redirect

# Create your views here.

from .forms import Reg_Form
from .models import Register

def output(request):
    if request.method == 'POST':
        form=Reg_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('details_list')
    else:
        form=Reg_Form()
    return render(request,'reg_details.html',{'form':form})

def view(request):
    details=Register.objects.all()
    return render(request,'detail_list.html',{'details':details})
    