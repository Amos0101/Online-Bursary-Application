from datetime import timezone

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class StudentApplication(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    STUDENT_STATUS_CHOICES = [
        ('KUCCPS', 'Government Sponsored (KUCCPS)'),
        ('PSSP', 'Self Sponsored (PSSP)')
    ]
    RESIDENTIAL_STATUS_CHOICES = [('Resident', 'Resident'), ('Non Resident', 'Non Resident')]

    COUNTY_CHOICES = [
        ('Nairobi', 'Nairobi'),
        ('Mombasa', 'Mombasa'),
        ('Kisumu', 'Kisumu'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    # Personal Details
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=50, unique=True)
    school = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    home_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    county = models.CharField(max_length=20, choices=COUNTY_CHOICES)
    next_of_kin = models.CharField(max_length=100)
    next_of_kin_address = models.CharField(max_length=255)
    next_of_kin_phone = models.CharField(max_length=15)
    chief_name = models.CharField(max_length=100)
    chief_address = models.CharField(max_length=255)
    chief_phone = models.CharField(max_length=15)
    disability = models.BooleanField(default=False)
    disability_details = models.CharField(max_length=255, blank=True, null=True)
    student_status = models.CharField(max_length=10, choices=STUDENT_STATUS_CHOICES)
    residential_status = models.CharField(max_length=15, choices=RESIDENTIAL_STATUS_CHOICES)

    # Family Background
    parental_status = models.CharField(max_length=10, choices=[
        ("both", "Have both parents"),
        ("one", "Have one parent"),
        ("orphan", "Total orphan"),
    ])

    death_certificate = models.FileField(upload_to="documents/", null=True, blank=True)

    # Father's Details
    father_age = models.IntegerField(null=True, blank=True)
    father_occupation = models.CharField(max_length=100, null=True, blank=True)
    father_employer = models.CharField(max_length=100, null=True, blank=True)
    father_health_status = models.FileField(upload_to="documents/", null=True, blank=True)

    # Mother's Details
    mother_age = models.IntegerField(null=True, blank=True)
    mother_occupation = models.CharField(max_length=100, null=True, blank=True)
    mother_employer = models.CharField(max_length=100, null=True, blank=True)
    mother_health_status = models.FileField(upload_to="documents/", null=True, blank=True)

    # Sibling Details
    total_siblings = models.IntegerField()
    university_siblings = models.IntegerField(null=True, blank=True)
    secondary_siblings = models.IntegerField(null=True, blank=True)
    out_of_school_siblings = models.IntegerField(null=True, blank=True)
    out_of_school_reason = models.TextField(null=True, blank=True)
    working_siblings_occupation = models.TextField(null=True, blank=True)

    # Other Information Fields
    school_fee_payer = models.CharField(max_length=255, blank=False, null=False)
    school_fee_evidence = models.FileField(upload_to="documents/", null=True, blank=True)

    work_study = models.CharField(max_length=3, choices=[("yes", "Yes"), ("no", "No")])
    work_study_evidence = models.FileField(upload_to="documents/", null=True, blank=True)

    external_support = models.CharField(max_length=3, choices=[("yes", "Yes"), ("no", "No")])
    sponsor_source = models.CharField(
        max_length=50, choices=[
            ("HELB", "HELB"),
            ("NGO", "NGO"),
            ("CDF", "CDF"),
            ("Other", "Other")], null=True,
        blank=True
    )
    sponsor_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    tuition_fee_paid = models.CharField(max_length=3, choices=[("yes", "Yes"), ("no", "No")])
    fee_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fee_statement = models.FileField(upload_to="documents/", null=True, blank=True)

    deferred_study = models.CharField(max_length=3, choices=[("yes", "Yes"), ("no", "No")])
    defer_reason = models.CharField(
        max_length=50,
        choices=[("Medical", "Medical"),
                 ("Social", "Social"),
                 ("Financial", "Financial"),
                 ("Academic", "Academic")],
        null=True, blank=True
    )

    additional_info = models.TextField(null=True, blank=True)
    additional_info_evidence = models.FileField(upload_to="documents/", null=True, blank=True)

    student = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to the student
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    submitted_at = models.DateTimeField(auto_now_add=True)  # Timestamp of submission
    reviewed_at = models.DateTimeField(null=True, blank=True)  # Timestamp when reviewed
    approved_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    def __str__(self):
        return f"{self.name} ({self.reg_no})"


class Notification(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)  # Notification belongs to a student
    message = models.TextField()  # Notification message
    is_read = models.BooleanField(default=False)  # Track if the notification is read
    created_at = models.DateTimeField(default=timezone.now)  # Time of creation

    def __str__(self):
        return f"Notification for {self.student.name} - {'Read' if self.is_read else 'Unread'}"