from django.db import models
# from django.utils import timezone
# Create your models here.


class Employee(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=191)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=191, null=True)
    phone = models.CharField(max_length=191, null=True)
    jd_id = models.IntegerField(null=True)
    qualification = models.CharField(max_length=100, null=True)
    marital_status_id = models.IntegerField(null=True)
    religion_id = models.IntegerField(null=True)
    address = models.TextField()
    experience = models.TextField()
    email = models.CharField(max_length=191, null=True)
    password = models.CharField(max_length=191, null=True)
    employee_id = models.CharField(max_length=191)
    branch_id = models.IntegerField(null=True)
    department_id = models.IntegerField(null=True)
    subdepartment_id = models.IntegerField(null=True)
    designation_id = models.IntegerField(null=True)
    category_id = models.IntegerField()
    company_doj = models.CharField(max_length=191, null=True)
    documents = models.CharField(max_length=191, null=True)
    account_holder_name = models.CharField(max_length=191, null=True)
    account_number = models.CharField(max_length=191, null=True)
    bank_name = models.CharField(max_length=191, null=True)
    ifsc_code = models.CharField(max_length=191, null=True)
    branch_location = models.CharField(max_length=191, null=True)
    aadhaar_no = models.CharField(max_length=50, null=True)
    pan_no = models.CharField(max_length=50, null=True)
    voter_id_no = models.CharField(max_length=50, null=True)
    driving_licence_no = models.CharField(max_length=50, null=True)
    uan_no = models.CharField(max_length=50, null=True)
    esi_no = models.CharField(max_length=50, null=True)
    tax_payer_id = models.CharField(max_length=191, null=True)
    salary_type = models.IntegerField(null=True)
    salary = models.FloatField(default=0)
    is_da = models.CharField(max_length=191, null=True)
    is_pf = models.CharField(max_length=191, null=True)
    is_esi = models.CharField(max_length=191, null=True)
    staff_category_id = models.IntegerField(null=True)
    holiday_eligible = models.CharField(max_length=191, null=True)
    is_active = models.IntegerField(default=1)
    cl_bal = models.IntegerField(default=0)
    sikl_bal = models.IntegerField(default=0)
    pl_bal = models.IntegerField(default=0)
    status = models.CharField(max_length=191, default='Active')
    notice_prd = models.IntegerField(null=True)
    regn_date = models.DateField(null=True)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
# class Meta:
#     managed = True
#     db_table = 'employee'
    def __str__(self):
        return f'{self.name}'

class Meta:
        db_table='app_employees'
