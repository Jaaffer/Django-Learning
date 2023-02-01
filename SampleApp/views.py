from django import http
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Student, File
from .forms import StudentForm, FileForm
from django.contrib import messages
import json
# Create your views here.


def home(request):
    student = Student.objects.all()
    context = {'student': student}
    return render(request, 'home.html', context)


def details(request, id):
    student_detail = get_object_or_404(Student, pk=id)
    context = {'student_detail': student_detail}
    return render(request, 'detail.html', context)


def create(request):
    context = {}
    form = StudentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    context['form'] = form
    return render(request, 'create.html', context)


def file():
    try:
        fileData = File.objects.last()
        if (str(fileData)[-4:] == 'json'):
            data = open(str(fileData))
            obj = json.load(data)
            firstname = obj['firstname']
            lastname = obj['lastname']
            username = obj['username']
            age = obj['age']
            email = obj['email']
            address = obj['address']
            phone_number = obj['phone_number']
            form = Student.objects.create(firstname=firstname, lastname=lastname, username=username,
                                          age=age, phone_number=phone_number, address=address, email=email)
            form.save()
        else:
            return 'File format is wrong or'
    except Exception as error:
        return error


def fileupload(request):
    if request.method == 'POST':
        file_form = FileForm(request.FILES)
        if file_form.is_valid() != True:
            filee = File(file=request.FILES['file'])
            filee.save()
            error = file()
            if (error):
                messages.warning(request, error)
            else:
                messages.success(request, 'Data added sucessfully')
                return redirect('/')
    else:
        file_form = FileForm()
    return render(request, 'file.html', {'form': file_form})


def bulk_file():
    try:
        fileData = File.objects.last()
        data = open(str(fileData))
        obj = json.load(data)
        # print(len(obj))
        for i in range(0, len(obj)):
            bulk_student = Student.objects.create(firstname=obj[i]['firstname'], lastname=obj[i]['lastname'], username=obj[i]
                                                ['username'], age=obj[i]['age'], email=obj[i]['email'], address=obj[i]['address'], phone_number=obj[i]['phone_number'])
            bulk_student.save()
    except Exception as error:
        return error  


def bulk_file_upload(request):
    if request.method == 'POST':
        file_form = FileForm(request.FILES)
        if file_form.is_valid() != True:
            filee = File(file=request.FILES['file'])
            filee.save()
            error = bulk_file()
            if (error):
                messages.warning(request, error)
            else:
                messages.success(request, 'Data added sucessfully')
                return redirect('/')
                
    else:
        file_form = FileForm()
    return render(request, 'file.html', {'form': file_form})
