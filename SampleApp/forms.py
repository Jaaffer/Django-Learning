from django import forms
from .models import Student, File

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = "__all__"

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = "__all__"