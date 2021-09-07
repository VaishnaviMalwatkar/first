from first.settings import DATABASES
# from app1.models import Employee
from app1.models import Pizza, Topping
# exec(open("C:\\Python\\.vscode\\Django\\first\\db_shell.py").read())
# emp = Employee(name="gaurav", salary=39.60, address="panvel")
# emp.save()
# all_data = Employee.objects.filter(id=4)

# print(all_data.query)



# emp = Employee(name="gaurav", salary=39.60, address="panvel")
# emp.save()
# import random
# my_list = ["pune", "mumbai", "kolkata", "bengalore", "hydrabad"]
# for i in range(1, 20):
#     Employee.objects.create(name=chr(65+i), salary=random.randint(30000, 60000), address=random.choice(my_list))

# fatch DATABASES

# all_data = list(Employee.objects.all())
# print(all_data)

# all_data = Employee.objects.all()
# print(all_data.query)

# get single data

# emp = Employee.objects.get(id=4)
# print(emp)

# emp = Employee.objects.filter(name="B")
# print(emp)

# total_sal = 0
# for i in Employee.objects.all():
#     total_sal += i.salary

# print(total_sal)


# def update_name_by_id(gname, ename):
#     # try:
#     emp = Employee.objects.get(name=gname)
#     emp.name = ename
#     emp.save()
#     print("successfully done...!")
#     # except Employee.DoesNotExist:
#     #     print("employee id does not exist...!")
        
# update_name_by_id("F", "FFF")

# def salary_increament(inc):
#     emp = Employee.objects.all()
#     for i in emp:
#         i.salary = i.salary + (i.salary*(inc/100))
#         i.save()
#     print("successfully done...!")

# salary_increament(30)

# Employee.objects.all().update(company="TC
# from datetime import date

# lic = License(license_key='MH26 54678654378', expiry_date=date(2021, 10, 10), dl_type="gwc", employee_id=20)
# lic.save()

# lice = License.objects.create(license_key='MH26 54678654377', expiry_date=date(2021, 10, 10), dl_type="gwc", employee_id=21)
# lice.save()
# emp = Employee.objects.get(id = 19)
# lic = License.objects.create(license_key='MH26 54678954378', expiry_date=date(2021, 10, 9), dl_type="gwc", employee = emp)
# lic.save()

# lic = License.objects.get(license_key="MH26 54678954378").employee_id
# print(lic)
# from datetime import date
# task = Task.objects.create(name = "create database")
# task.employee_id = 2
# task.save()

# exec(open("C:\\Python\\.vscode\\Django\\first\\db_shell.py").read())

pizza = Pizza.objects.create(name="hiwia")
t1 = Topping.objects.get(id=15)
t2 = Topping.objects.get(id=16)
t1.save()
t2.save()
 
pizza.topping.add(t1)   
pizza.topping.add(t2)                                

print(pizza.topping.all())