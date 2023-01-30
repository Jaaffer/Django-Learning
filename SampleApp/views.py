from pyexpat.errors import messages
from django import http
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
# Create your views here.

def home(request):
    student = Student.objects.all()
    context = {'student': student}
    return render(request, 'home.html', context)

def details(request, id):
    student_detail = get_object_or_404(Student, pk=id)
    context = {'student_detail':student_detail}
    return render(request, 'detail.html', context)

def create(request):
    context = {}
    form = StudentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    context['form'] = form
    return render(request, 'create.html',context)