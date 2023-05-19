from django.shortcuts import render
from django.http import HttpResponse
# from django.utils import timezone
# from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm #add this
#login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
#register
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from .models import Employee
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from app.serializers import EmployeeSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from knox.auth import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


# Create your views here.
def app(request):
    return HttpResponse("Hello world!")

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'myapp/login.html'
    
    def get_success_url(self):
        return reverse_lazy('tasks') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class KnoxLoginView(LoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        # Retrieve additional information about the user
        user_data = {'user-admin': user.username, 'email': user.email, 'id' :user.id}
        return Response({
            'user': user_data,
            'token': AuthToken.objects.create(user)[1],
            'message': 'Login successful'
        })













# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    
# @api_view(['POST'])
# def get_employee_detail(request):
#     employee_data = request.data
#     employee = Employee.objects.get(**employee_data)
#     serializer = EmployeeSerializer(employee)
#     return Response(serializer.data)
# @api_view(['POST'])
# def get_employee_detail(request):
#     employee_data = request.data
#     employee = Employee.objects.filter(**employee_data).first()
#     if employee:
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data)
#     else:
#         return Response({"message": "Employee not found"})

# @api_view(['GET'])
# def employee_view(request):
#     employees = Employee.objects.all()
   
#     serializer = EmployeeSerializer(employees, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def get_employee_detail(request):
#     employee_id = request.query_params.get('user_id')
#     employee = Employee.objects.get(id=employee_id)
#     serializer = EmployeeSerializer(employee)
#     return Response(serializer.data)

    
# @api_view(['GET'])
# def get_employee_detail(request, pk):
#     employee = Employee.objects.get(pk=pk)
#     serializer = EmployeeSerializer(employee)
#     return Response(serializer.data)

    
class EmployeeList(APIView):
    def get(self, request):
        employee_id = request.GET.get('id')
        if employee_id:
            employee = Employee.objects.get(pk=employee_id)
            serializer = EmployeeSerializer(employee)
            data = {"status": "success", "employees": serializer.data}
        else:
            data = {"message": "Employee not found"}
            return Response(serializer.data)
        return Response(data=data, status=status.HTTP_200_OK)
       
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        data = {"status": "success", "employees": serializer.data}
        return Response(data=data, status=status.HTTP_200_OK)
        return Response(serializer.data)

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        data = {"status": "success", "employees": serializer.data}
        return Response(data=data, status=status.HTTP_200_OK)
 

    # def employee_detail(request, employee_id):
    #     employee = get_object_or_404(Employee, pk=employee_id)
    #     context = {'employee': employee}
    #     return render(request, 'employee_detail.html', context)

@api_view(['GET'])
def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)


class EmployeeDetail(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'
