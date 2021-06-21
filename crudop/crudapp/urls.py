from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('<int:id>/',views.home,name="emp_update"),
    path('register/',views.employee_register,name="register")
]