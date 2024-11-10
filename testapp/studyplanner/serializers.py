from rest_framework import serializers
import os
from pathlib import Path
from .models import Company ,Employee


# Create Serializers here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"

