from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

def home(request):
    if request.method == 'POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form=EmployeeForm()
    return render(request, 'index.html',{'form':form})
def show(request):
    emp=Employee.objects.all()
    return render(request, 'show.html',{'emp':emp})
def delete(request,id):
    obj=Employee.objects.get(id=id)
    obj.delete()
    return redirect('/show')
def update(request,id):
    obj=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html',{'emp':obj})

        
    


