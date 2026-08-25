from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import StudentForm
from .models import Student
@login_required
def student_list(request):
    query = request.GET.get("q", "").strip()
    students = Student.objects.all()

    if query:
        students = students.filter(name__icontains=query) | students.filter(
            email__icontains=query
        ) | students.filter(course__icontains=query)

    return render(request, "students/student_list.html", {
        "students": students,
        "query": query,
    })
@login_required
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully.")
            return redirect("student_list")
    else:
        form = StudentForm()

    return render(request, "students/student_form.html", {
        "form": form,
        "title": "Add Student",
        "button": "Add Student",
    })
@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully.")
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)

    return render(request, "students/student_form.html", {
        "form": form,
        "title": "Edit Student",
        "button": "Update Student",
    })
@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully.")
        return redirect("student_list")

    return render(request, "students/student_confirm_delete.html", {
        "student": student,
    })
