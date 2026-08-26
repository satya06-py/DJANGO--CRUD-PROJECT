from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import StudentForm
from .models import Student, Attendance


@login_required
def student_list(request):
    # Get search query
    query = request.GET.get("q", "").strip()

    # Get all students
    students = Student.objects.all().order_by("id")

    # Search students by name, email, or course
    if query:
        students = (
            students.filter(name__icontains=query)
            | students.filter(email__icontains=query)
            | students.filter(course__icontains=query)
        )

    # Pagination: 5 students per page
    paginator = Paginator(students, 5)

    # Get current page number
    page_number = request.GET.get("page")

    # Get page object
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "students/student_list.html",
        {
            "students": page_obj,
            "page_obj": page_obj,
            "query": query,
        },
    )


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

    return render(
        request,
        "students/student_form.html",
        {
            "form": form,
            "title": "Add Student",
            "button": "Add Student",
        },
    )


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

    return render(
        request,
        "students/student_form.html",
        {
            "form": form,
            "title": "Edit Student",
            "button": "Update Student",
        },
    )


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully.")
        return redirect("student_list")

    return render(
        request,
        "students/student_confirm_delete.html",
        {
            "student": student,
        },
    )


# =========================
# ATTENDANCE
# =========================

@login_required
def attendance(request):
    # Get all students
    students = Student.objects.all().order_by("name")

    # Save attendance
    if request.method == "POST":

        date = request.POST.get("date")

        for student in students:

            status = request.POST.get(
                f"student_{student.id}"
            )

            Attendance.objects.update_or_create(
                student=student,
                date=date,
                defaults={
                    "present": status == "present"
                },
            )

        messages.success(
            request,
            "Attendance saved successfully."
        )

        return redirect("attendance")

    # Today's date
    today = timezone.localdate()

    return render(
        request,
        "students/attendance.html",
        {
            "students": students,
            "today": today,
        },
    )