from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (LaptopMovementViewSet, LaptopViewSet, StudentViewSet, home,
                    laptop_movements, laptops, new_laptop, new_laptop_movement,
                    new_student, students)

# r'schools'  This is the URL pattern that will be used for accessing the API endpoint associated with the SchoolViewSet viewset. The r prefix before the string indicates a raw string literal, which is often used in regular expressions and URL patterns to avoid escaping special characters.


router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'laptops', LaptopViewSet)
router.register(r'laptop-movements', LaptopMovementViewSet) 

urlpatterns = [
    path('apis/', include(router.urls)),
    path("", home, name="home"),
    path("laptops/", laptops, name="laptops"),
    path("new-laptop/", new_laptop, name="new-laptop"),
    path("students/", students, name="students"),
    path("new-student/", new_student, name="new-student"),
    path("laptop-movements/", laptop_movements, name="laptop-movements"),
    path("new-checkin/", new_laptop_movement, name="new-checkin"),
]
 