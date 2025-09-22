from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def add_student(request):
    if request.method == 'POST':
        # Here you would typically handle the form submission,
        # validate the data, and save it to the database.
        # For now, we will just print the data to the console.

        data = request.POST

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        student_id = data.get('student_id')
        email = data.get('email')
        dob = data.get('dob')
        course = data.get('course')
        year = data.get('year')
        profile_picture = request.FILES.get('profile_picture', None)

        # print(f"First Name: {first_name}")
        # print(f"Last Name: {last_name}")
        # print(f"Student ID: {student_id}")
        # print(f"Email: {email}")
        # print(f"DOB: {dob}")
        # print(f"Course: {course}")
        # print(f"Year: {year}")

        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            student_id=student_id,
            email=email,
            dob=dob,
            course=course,
            year=year,
            profile_picture=profile_picture
        )

        return redirect('/add_student') 
    
    return render(request, 'add_student.html')

def students(request):

    queryset = Student.objects.all()

    search_query = request.GET.get('search', None)
    if search_query:
        queryset = queryset.filter(
            student_id__icontains=search_query
        ) | queryset.filter(
            first_name__icontains=search_query
        ) | queryset.filter(
            last_name__icontains=search_query
        )
    context = {
        'students': queryset
    }
    return render(request, 'students.html', context)

def delete_student(request, student_id):
    queryset = Student.objects.get(id=student_id)
    queryset.delete()
    return redirect('/students')

def update_student(request, student_id):
    queryset = Student.objects.get(id=student_id)

    if request.method == 'POST':
        # Here you would typically handle the form submission,
        # validate the data, and save it to the database.
        # For now, we will just print the data to the console.

        data = request.POST

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        student_id = data.get('student_id')
        email = data.get('email')
        dob = data.get('dob')
        course = data.get('course')
        year = data.get('year')
        profile_picture = request.FILES.get('profile_picture')

        queryset.first_name = first_name
        queryset.last_name = last_name
        queryset.student_id = student_id
        queryset.email = email
        queryset.dob = dob
        queryset.course = course
        queryset.year = year
        if profile_picture:
            queryset.profile_picture = profile_picture
        queryset.save()

        return redirect('/students/')
    
    context = {'student': queryset}
    return render(request, 'update_student.html', context)

def reports(request):
    return render(request, 'reports.html')