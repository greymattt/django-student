from django.shortcuts import render, redirect
from admissionapp.forms import StudentForm
from admissionapp.models import Student

# Create your views here.


def home(request):
    return render(request, "admissionapp/home.html")


def studform(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            print("HELLO")
            form.save()
            print("AFTER SAVE")
            return redirect('/home')

    else:
        form = StudentForm()
    return render(request, 'admissionapp/create.html', {'form': form})


def show(request):
    students = Student.objects.all()
    return render(request, "admissionapp/show.html", {"students": students})


def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'admissionapp/edit.html', {'student': student})


def update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'employee/edit.html', {'employee': student})


def erase(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("/home")


def display(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'admissionapp/display.html', {'student': student})


def filter(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'admissionapp/filter.html', {'student': student})
