from django.shortcuts import render, redirect
from .models import Students
from .forms import StudentForm

def readStudents(request):
    students = Students.objects.all()
    return render(request, 'students.html',{'students':students})

def addStudent(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('readStudents')

    return render(request, 'newStudent.html',{'form':form})

def updateStudent(request, id):
    student = Students.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('readStudents')
    return render(request, 'newStudent.html', {'form':form, 'student':student})

def deleteStudent(request, id):
    student = Students.objects.get(id=id)

    if request.method=='POST':
        student.delete()
        return redirect('readStudents')
    return render(request, 'deleteStudent.html', {'student':student})
