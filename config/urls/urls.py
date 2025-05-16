from django.urls import path
from cmanager_tenant.admin import tenant_admin_site

urlpatterns = [
    path('admin/', tenant_admin_site.urls),
]
