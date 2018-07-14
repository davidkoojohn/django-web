from django.db import models

class Dept(models.Model):
  """部门类"""

  no = models.IntegerField(primary_key=True, db_column='dno', verbose_name='部门编号')
  name = models.CharField(max_length=20, db_column='dname', verbose_name='部门名称')
  location = models.CharField(max_length=10, db_column='dloc', verbose_name='部门所在地')

  class Meta:
    db_table = 'tb_dept'

class Emp(models.Model):
  """员工类"""

  no = models.IntegerField(primary_key=True, db_column='eno', verbose_name='员工编号')
  name = models.CharField(max_length=20, db_column='ename', verbose_name='员工姓名')
  job = models.CharField(max_length=10, verbose_name='职位')

  mgr = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='主管编号')
  sal = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='月薪')
  comm = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='补贴')

  dept = models.ForeignKey(Dept, db_column='dno', on_delete=models.PROTECT, verbose_name='所在部门')

  class Meta:
    db_table = 'tb_emp'

# IntegerField = integer类型
# CharField    = varchar类型
# DecimalField = decimal类型
# ForeignKey   = 用来建立多对一外键关联
# primary_key  = 用于设置主键
# max_length
# db_column
# verbose_name = Django后台管理系统中该字段显示的名称
