from django.db import models


class Student(models.Model):
    Stu_name = models.CharField(max_length=100)
    Stu_email = models.EmailField()
    Stu_address = models.CharField(max_length=200, null=True, blank=True)
    Stu_dis = models.TextField(null=True, blank=True)
    Stu_contact = models.CharField(max_length=15)
    Stu_dob = models.DateField()
    Stu_qualification = models.CharField(max_length=100, null=True, blank=True)
    Stu_gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    Stu_image = models.ImageField(upload_to='students/')
    Stu_document = models.FileField(upload_to='documents/', null=True, blank=True)
    Stu_password = models.CharField(max_length=255)


    # def __str__(self):
    #     return self.Stu_name
