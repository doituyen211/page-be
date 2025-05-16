from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from .models import Tenant, Domain


class TenantAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('schema_name', 'name', 'is_active')
    search_fields = ('schema_name', 'name')
    list_filter = ('is_active',)
    ordering = ('schema_name',)
    list_per_page = 10
    actions = ['activate_tenant', 'deactivate_tenant']

    def activate_tenant(self, request, queryset):
        queryset.update(is_active=True)

    def deactivate_tenant(self, request, queryset):
        queryset.update(is_active=False)

    activate_tenant.short_description = "Activate selected tenants"
    deactivate_tenant.short_description = "Deactivate selected tenants"
    
    
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant', 'is_primary')
    search_fields = ('domain',)
    list_filter = ('is_primary',)
    ordering = ('domain',)
    list_per_page = 10
    actions = ['make_primary']

    def make_primary(self, request, queryset):
        queryset.update(is_primary=True)

    make_primary.short_description = "Make selected domains primary"
    

class TenantAdminSite(admin.AdminSite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.site_header = "Tenant Admin"
        self.site_title = "Tenant Admin"
        self.index_title = "Tenant Admin"
        self.register(Tenant, TenantAdmin)
        self.register(Domain, DomainAdmin)
        
        
tenant_admin_site = TenantAdminSite(name='tenant_admin')