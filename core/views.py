from django.shortcuts import render
from .models import HomePage, Department, Specialty, ExchangeProgram

def home(request):
    page_data = HomePage.objects.first() 
    return render(request, 'home.html', {'page': page_data})

def programs(request):
    all_programs = Specialty.objects.all()
    return render(request, 'programs.html', {'programs': all_programs})

def program_detail(request, id):
    program = Specialty.objects.get(id=id)
    return render(request, 'program_detail.html', {'program': program})

def departments(request):
    all_deps = Department.objects.all()
    return render(request, 'departments.html', {'departments': all_deps})

def department_detail(request, id):
    department = Department.objects.get(id=id)
    teachers = department.teacher_set.all()
    specialties = department.specialty_set.all()
    return render(request, 'department_detail.html', {
        'department': department, 'teachers': teachers, 'specialties': specialties
    })

def admission(request):
    return render(request, 'admission.html')

def exchange(request):
    programs = ExchangeProgram.objects.all()
    return render(request, 'exchange.html', {'programs': programs})