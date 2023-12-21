from django.shortcuts import render, redirect
from .models import StudentRecord, AdminInformation
from .forms import DataForm, AdminData
# Create your views here.


def StudentRecordAdd(request):
    users = StudentRecord.objects.all().values()
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            address = form.cleaned_data['address']
            user = StudentRecord(name=name, age=age, address=address)
            user.save()

            return render(request, 'index.html', {'form': DataForm, 'users': users})
    else:
        return render(request, 'index.html', {'form': DataForm, 'users': users})


def AdminRecordAdd(request):
    admin = AdminInformation.objects.all().values()
    if request.method == "POST":
        forms = AdminData(request.POST)
        if forms.is_valid():
            print(forms)
            forms.save()
            return redirect('admins')
    else:
        return render(request, 'admin.html', {'form': AdminData, 'admins': admin})
