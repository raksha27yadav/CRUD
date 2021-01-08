from django.shortcuts import render,redirect
from .forms import credaddform
from .models import Address
def CredentialForm(request,id=0):
    if request.method=="GET":
        if id==0:
           form=credaddform()
        else:
            address=Address.objects.get(pk=id)
            form=credaddform(instance=address)
        return render(request,'crudapp/credform.html',{'form':form})
    else:
        if id==0:
            form=credaddform(request.POST)
        else:
            address=Address.objects.get(pk=id)
            form=credaddform(request.POST,instance=address)
        if form.is_valid():
            form.save()
        return redirect('/credential/list')
        
def credList(request):
    list=Address.objects.all()
    return render(request,'crudapp/credlist.html',{'list':list})

def creddelete(request,id):
    if request.method=="POST":
       address=Address.objects.get(pk=id)
       address.delete()
       return redirect('/credential/list')
    
    