from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from students.models import StudentApplication, Notification


def admin_homepage(request):
    return render(request,'admin_homepage.html')
def review_applications(request):
    # Fetch all applications with status 'Pending'
    pending_apps = StudentApplication.objects.filter(status='Pending').order_by('-submitted_at')

    return render(request, 'review_applications.html', {'pending_apps': pending_apps})

def review_application_details(request, app_id):
    application = get_object_or_404(StudentApplication, id=app_id)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'approve':
            application.status = 'Approved'
            Notification.objects.create(student=application.student, message="Your application has been approved!")
            messages.success(request, "Application approved successfully.")
        elif action == 'reject':
            application.status = 'Rejected'
            Notification.objects.create(student=application.student, message="Your application was rejected.")
            messages.warning(request, "Application rejected.")

        application.save()
        return redirect('review_applications')  # Redirect back to pending applications

    return render(request, 'review_details.html', {'application': application})


def approved_applications(request):
    approved_apps = StudentApplication.objects.filter(status="Approved")
    return render(request, 'approved_applications.html', {'approved_apps': approved_apps})


def rejected_applications(request):
    rejected_apps = StudentApplication.objects.filter(status="Rejected")
    return render(request, 'rejected_applications.html', {'rejected_apps': rejected_apps})