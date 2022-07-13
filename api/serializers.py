from rest_framework import serializers as s

from .models import Employee


class EmployeeSerializer(s.ModelSerializer):
    class Meta:
        model = Employee
        # fields = [
        #     'firstname', 'lastname', 'position', 'date_submitted', 'salary', 'ref_employee'
        # ]
        fields = '__all__'
