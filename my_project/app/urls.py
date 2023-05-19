from django.urls import path
from . import views
from .views import MyLoginView

from .views import RegisterAPI

from knox import views as knox_views
from .views import LoginAPI
from .views import EmployeeList, EmployeeDetail
# from .views import StatusAPIView


urlpatterns = [
    path('app/', views.app, name='app'),
    path('login/', MyLoginView.as_view(),name='login'),

    path('api/login/',  LoginAPI.as_view(), name='login'),
    # path('api/login/', KnoxLoginView.as_view(), name='knox_login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('employees/', EmployeeList.as_view()),
    path('employees/<int:pk>/', EmployeeDetail.as_view()),
    # path('employee/<int:employee_id>/', employee_detail, name='employee_detail'),

    # path('employee/', views.get_employee_detail, name='get_employee_detail'),
    # path('success/', StatusAPIView.as_view(), name='success'),
]