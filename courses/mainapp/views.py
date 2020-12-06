from django.shortcuts import render, redirect
from .models import Courses, Student
from .forms import StudentForm
from django.views.generic import DetailView
from django.contrib import messages


def index(request):
    courses = Courses.objects.all()
    return render(request, 'mainapp/index.html', {'title': 'Главная страница', 'courses': courses})


class CourseDetailView(DetailView):
    model = Courses
    template_name = 'mainapp/detail_course.html'
    context_object_name = 'course'


def teacher(request):
    courses = Courses.objects.all()
    return render(request, 'mainapp/teacher.html', {'title': 'Преподаватели', 'courses': courses})


def group(request):
    group = Courses.objects.all()
    student = Student.objects.all()
    return render(request, 'mainapp/group.html', {'title': 'Группы', 'group': group, 'student': student})


def ditail_group(request):
    group = Courses.objects.all()
    student = Student.objects.all()
    return render(request, 'mainapp/ditail_group.html', {'title': 'Ученики', 'group': group, 'student': student})

# здесь менял
# class StudentDetailView(DetailView):
#     model = Student
#     template_name = 'mainapp/ditail_group'
#     context_object_name = 'student'


def create(request):
    error = ''
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = StudentForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'mainapp/create.html', context)
