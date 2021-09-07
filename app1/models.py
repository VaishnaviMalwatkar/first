from django.db import models

# Create your models here.
class Common(models.Model):
    
    def __str__(self):
        return f"{self.__dict__}"
    
    def __repr__(self):
        return str(self)

    class Meta:
        abstract = True

class Employee(Common):
    name = models.CharField(max_length=100)
    salary = models.FloatField()
    address = models.CharField(max_length=50)
    company = models.CharField(max_length=50, default=None)

    class Meta:
        db_table = "emp"
   
    def ge_salary_grom_name(self):
        return f"{self.name} having {self.salary} in database"  

class License(Common):
    license_key = models.CharField(primary_key=True, max_length=16)
    expiry_date = models.DateField() 
    dl_type = models.CharField(max_length=20)
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE)   

    class Meta:
        db_table = "license"

class Task(Common):
    task_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    timeline = models.DateTimeField(null=True)
    task_create_date = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "task"



class Topping(Common):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "topping"


class Pizza(Common):
    name = models.CharField(max_length=100)
    topping = models.ManyToManyField('Topping', related_name="pizzas")

    class Meta:
        db_table = "pizza"



