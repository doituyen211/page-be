from django.db import models
import uuid
from cmanager_tenant.models import Tenant
from core.models import User


class Student(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('graduated', 'Graduated'),
        ('transferred', 'Transferred'),
        ('suspended', 'Suspended'),
        ('on-leave', 'On-Leave'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=50, unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20)
    address = models.TextField()
    enrollment_date = models.DateField()
    # current_class = models.ForeignKey('classes.Class', on_delete=models.SET_NULL, null=True, blank=True)
    # blood_group = models.CharField(max_length=10, blank=True)
    parent_info = models.JSONField(default=dict, blank=True)
    # emergency_contact = models.CharField(max_length=50, blank=True)
    # medical_info = models.TextField(blank=True)
    current_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    previous_school = models.CharField(max_length=255, blank=True)
    previous_school_id = models.CharField(max_length=50, blank=True)
    entry_grade_level = models.IntegerField()
    exit_grade_level = models.IntegerField(null=True, blank=True)
    # transfer_reference = models.ForeignKey('tenant_manager.TransferRequest', on_delete=models.SET_NULL, null=True, blank=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_id

    class Meta:
        db_table = 'student'