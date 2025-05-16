from django.db import models
import uuid
from cmanager_tenant.models import Tenant
from core.models import User

    
    
class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=50, unique=True)
    # department = models.ForeignKey('classes.Department', on_delete=models.SET_NULL, null=True)
    qualification = models.TextField(blank=True)
    joined_date = models.DateField()
    specialization = models.CharField(max_length=100, blank=True)
    is_class_teacher = models.BooleanField(default=False)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_id

    class Meta:
        db_table = 'teacher'