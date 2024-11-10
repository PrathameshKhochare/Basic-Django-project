# from django.urls import path
# from . import views

### localhost:8000\studyplanner\index
# urlpatterns = [
#     path('index' ,views.index)
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('studyplanner/' ,include("studyplanner.urls"))

######
from django.contrib import admin
from django.urls import path,include
from .views import CompanyViewSet , EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('' ,include(router.urls))
         ]
