from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.v1.school.views import StudentViewSet

router = DefaultRouter()
router.register(r'student', StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/school/', include(router.urls)),
]
