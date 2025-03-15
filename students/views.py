from django.contrib import messages
from .forms import StudentApplicationForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def student_dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def homepage(request):
    return render(request, 'homepage.html')


def student_application(request):
    if request.method == "POST":
        form = StudentApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Application submitted successfully!")
            return redirect("application_success")  # Redirect to success page
        else:
            messages.error(request, "There were errors in your form. Please check and submit again.")
    else:
        form = StudentApplicationForm()

    return render(request, "student_application.html", {"form": form})

def confirm_application(request):
    form_data = request.session.get('form_data', {})
    file_data = request.session.get('file_data', {})

    if request.method == "POST":
        form = StudentApplicationForm(form_data, file_data)
        if form.is_valid():
            form.save()

            # Clear session after saving
            del request.session['form_data']
            del request.session['file_data']

            messages.success(request, "Application submitted successfully!")  # Flash success message
            print("Redirecting to success page...")
            return redirect('application_success')  # Redirect to success page

        else:
            messages.error(request, "An error occurred. Please try again.")

    return render(request, 'confirm_application.html', {'form_data': form_data, 'file_data': file_data})