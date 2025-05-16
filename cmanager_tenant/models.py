from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Tenant(TenantMixin):
    """
    This is the tenant model. It inherits from TenantMixin, which provides
    the necessary fields and methods for a tenant in a multi-tenant setup.
    """
    TYPE_CHOICES = (
        ('s', 'school'),
        ('a', 'academy'),
        ('t','tutor'),
    )
    name = models.CharField(max_length=100)
    schema_name = models.CharField(max_length=100, unique=True)
    domain_url = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    # auto_create_schema = True

    def __str__(self):
        return self.name

class Domain(DomainMixin):
    pass