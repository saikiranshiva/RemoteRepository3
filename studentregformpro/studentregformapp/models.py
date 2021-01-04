from django.db import models
class StudentData(models.Model):
    roll_number=models.IntegerField(primary_key=True)
    student_name=models.CharField(max_length=100)
    mobile_number=models.BigIntegerField()
    fee=models.IntegerField()
    email=models.EmailField(max_length=100)
    dateofbirth=models.DateField(max_length=100)
    gender=models.CharField(max_length=100)
    courses=models.CharField(max_length=100)
    institute_name=models.CharField(max_length=100)
    address=models.TextField(max_length=500)

