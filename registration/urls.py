from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import SchoolViewSet, StudentViewSet, LaptopViewSet, LaptopRegistrationViewSet, TheftReportViewSet

# r'schools'  This is the URL pattern that will be used for accessing the API endpoint associated with the SchoolViewSet viewset. The r prefix before the string indicates a raw string literal, which is often used in regular expressions and URL patterns to avoid escaping special characters.


router = DefaultRouter()
router.register(r'schools', SchoolViewSet) 
router.register(r'students', StudentViewSet) 
router.register(r'laptops', LaptopViewSet) 
router.register(r'laptop-registration', LaptopRegistrationViewSet) 
router.register(r'theft-reports', TheftReportViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]
 