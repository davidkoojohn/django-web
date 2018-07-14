```
(venv)$ python manage.py shell
# create
>>> from hrs.models import Dept, Emp
>>> dept = Dept(40, '研发2部', '深圳')
>>> dept.save()

# update 
>>> dept.name = '研发3部'
>>> dept.save()

# view
>>> Dept.objects.all()

# filter

>>> Dept.objects.filter(name='研发3部')
# 查询部门名称包含“研发”的部门(模糊查询)
>>> Dept.objects.filter(name__contains='研发')
# 查询部门编号大于10小于40的部门
>>> Dept.objects.filter(no__gt=10).filter(no__lt=40) 
# 查询部门编号在10到30之间的部门
>>> Dept.objects.filter(no__range=(10, 30)) 

# take one
>>> Dept.objects.get(pk=10)
>>> Dept.objects.get(no=20)
Dept.objects.get(no__exact=30)

# sort list
>>> Dept.objects.order_by('no') # 查询所有部门按部门编号升序排列
>>> Dept.objects.order_by('-no') # 查询所有部门按部门编号降序排列

# cut data
>>> Dept.objects.order_by('no')[0:2] # 按部门编号排序查询1~2部门
>>> Dept.objects.order_by('no')[2:4] # 按部门编号排序查询3~4部门

# 
>>> Emp.objects.filter(dept__no=10) # 根据部门编号查询该部门的员工
>>> Emp.objects.filter(dept__name__contains='销售') # 查询名字包含“销售”的部门的员工
>>> Dept.objects.get(pk=10).emp_set.all() # 通过部门反查部门所有的员工

# delete
>>> Dept.objects.get(pk=40).delete()
```