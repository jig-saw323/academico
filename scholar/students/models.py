
from tkinter import CASCADE
from django.db import models
from  django.utils import timezone
import datetime
# Create your models here.
class User(models.Model):
    email=models.CharField(max_length=100)
    
    password=models.CharField(max_length=500)

    status=models.BooleanField( null= True)

    created_at=models.DateTimeField(default= datetime.datetime.now, null=False)

    update_at=models.DateTimeField(default= datetime.datetime.now, null=False)

    delete_at=models.DateTimeField(null= True)

# Create your models here.
class Students(models.Model):
    code=models.CharField(max_length=50, null=False)
    
    id_person=models.IntegerField(null=False)

    status=models.BooleanField( null= True)

    created_at=models.DateTimeField(default= datetime.datetime.now, null=False)

    update_at=models.DateTimeField(default= datetime.datetime.now, null=False)

    delete_at=models.DateTimeField(null= True)



# Create your models here.
class Identification_types(models.Model):
    name=models.CharField(max_length=50, null=False)

    abrev=models.CharField(max_length=10, null=False)
    
    descrip=models.CharField(max_length=100, null=False)

    created_at=models.DateTimeField(default= datetime.datetime.now, null=False)

    update_at=models.DateTimeField(default= datetime.datetime.now, null=False)

    delete_at=models.DateTimeField(null= True)

# Create your models here.
class Persons(models.Model):
    first_name=models.CharField(max_length=50, null=False)

    last_name=models.CharField(max_length=50, null=False)

    id_ident_type=models.IntegerField( null= False)

    ident_number=models.CharField(max_length=15, null=False)

    id_exp_city =models.IntegerField( null= False)

    address=models.CharField(max_length=150, null=False)
    
    mobile=models.CharField(max_length=50, null=False)

    id_user =models.ForeignKey( User,on_delete= CASCADE)

    created_at=models.DateTimeField(default= datetime.datetime.now, null=False)

    update_at=models.DateTimeField(default= datetime.datetime.now, null=False)

    delete_at=models.DateTimeField(null= True)


# Create your models here.
class Cities(models.Model):
    name=models.CharField(max_length=100, null=False)

    abrev=models.CharField(max_length=10, null=False)

    descrip=models.CharField(max_length=100, null=False)

    ident_number=models.CharField(max_length=15, null=False)

    id_dept =models.IntegerField( null= False)

    created_at=models.DateTimeField(default= datetime.datetime.now, null=False)

    update_at=models.DateTimeField(default= datetime.datetime.now, null=False)

    delete_at=models.DateTimeField(null= True)

# Create your models here.
class Departments(models.Model):
    name=models.CharField(max_length=100, null=False)

    abrev=models.CharField(max_length=10, null=False)

    descrip=models.CharField(max_length=100, null=False)

    ident_number=models.CharField(max_length=15, null=False)

    id_country =models.IntegerField( null= False)

    created_at=models.DateTimeField(default= datetime.datetime.now, null=False)

    update_at=models.DateTimeField(default= datetime.datetime.now, null=False)

    delete_at=models.DateTimeField(null= True)

# Create your models here.
class Countries(models.Model):
    name=models.CharField(max_length=100, null=False)

    abrev=models.CharField(max_length=10, null=False)

    descrip=models.CharField(max_length=100, null=False)

    ident_number=models.CharField(max_length=15, null=False)

    created_at=models.DateTimeField(default= datetime.datetime.now, null=False)

    update_at=models.DateTimeField(default= datetime.datetime.now, null=False)

    delete_at=models.DateTimeField(null= True)
