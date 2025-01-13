from django.shortcuts import render,redirect

# Create your views here.

from .forms import Reg_Form
from .models import Register

def output(request):
    if request.method == 'POST':
        form=Reg_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('view')
    else:
        form=Reg_Form()
    return render(request,'reg_detail.html',{'form':form})

def view(request):
    images=Register.objects.all()
    return render(request,'detail_list.html',{'images':images})

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import os

def dnld_img(request,pk):
    image_instance=get_object_or_404(Register,pk=pk)
    image_path=image_instance.image.path
    with open (image_path,'rb')as f:
        response=HttpResponse(f.read(),content_type="application/octet-stream")
        response['content disposition']=f'attachment; filename={os.path.basename(image_path)}'
        return response
