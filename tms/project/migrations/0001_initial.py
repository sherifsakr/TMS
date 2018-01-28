# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-25 17:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApfDeptView',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('dept_code', models.CharField(blank=True, db_column='DEPT_CODE', max_length=5, null=True, unique=True)),
                ('dept_name', models.CharField(blank=True, db_column='DEPT_NAME', max_length=100, null=True)),
                ('resp_dept_name', models.CharField(blank=True, db_column='RESP_DEPT_NAME', max_length=100, null=True)),
                ('manager_title', models.CharField(blank=True, db_column='MANAGER_TITLE', max_length=100, null=True)),
                ('manager_ext', models.CharField(blank=True, db_column='MANAGER_EXT', max_length=100, null=True)),
                ('manager_name', models.CharField(blank=True, db_column='MANAGER_NAME', max_length=100, null=True)),
                ('manager_code', models.CharField(blank=True, db_column='MANAGER_CODE', max_length=20, null=True)),
                ('note', models.CharField(blank=True, db_column='NOTE', max_length=200, null=True)),
                ('city_name', models.CharField(blank=True, db_column='CITY_NAME', max_length=100, null=True)),
                ('city_code', models.CharField(blank=True, db_column='CITY_CODE', max_length=20, null=True)),
                ('branch_name', models.CharField(blank=True, db_column='BRANCH_NAME', max_length=100, null=True)),
                ('branch_code', models.IntegerField(blank=True, db_column='BRANCH_CODE', null=True)),
            ],
            options={
                'db_table': 'apf_dept_view',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Delegation',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('deptauthcode', models.CharField(blank=True, db_column='DeptAuthCode', max_length=10, null=True)),
                ('start', models.DateTimeField(blank=True, db_column='Start', null=True)),
                ('end', models.DateTimeField(blank=True, db_column='End', null=True)),
                ('expired', models.CharField(blank=True, db_column='Expired', max_length=1, null=True)),
            ],
            options={
                'db_table': 'delegation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('deptname', models.CharField(blank=True, db_column='DeptName', max_length=200, null=True, unique=True)),
                ('managerid', models.CharField(blank=True, db_column='ManagerId', max_length=45, null=True)),
                ('deptcode', models.IntegerField(blank=True, db_column='DeptCode', null=True, unique=True)),
            ],
            options={
                'db_table': 'department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField(db_column='EmpId', unique=True)),
                ('empname', models.CharField(blank=True, db_column='EmpName', max_length=255, null=True)),
                ('deptcode', models.CharField(blank=True, db_column='DeptCode', max_length=45, null=True)),
                ('deptname', models.CharField(blank=True, db_column='DeptName', max_length=200, null=True)),
                ('ismanager', models.IntegerField(blank=True, db_column='IsManager', null=True)),
                ('ext', models.CharField(blank=True, db_column='Ext', max_length=45, null=True)),
                ('mobile', models.CharField(blank=True, db_column='Mobile', max_length=45, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=100, null=True)),
                ('jobtitle', models.CharField(blank=True, db_column='JobTitle', max_length=200, null=True)),
                ('managercode', models.BigIntegerField(blank=True, db_column='ManagerCode', null=True)),
                ('sexcode', models.CharField(blank=True, db_column='SexCode', max_length=6, null=True)),
                ('iscontract', models.IntegerField(blank=True, db_column='IsContract', null=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=250)),
                ('start', models.DateField(db_column='Start')),
                ('end', models.DateField(db_column='End')),
                ('teamname', models.CharField(blank=True, db_column='TeamName', max_length=100, null=True)),
                ('desc', models.CharField(db_column='Desc', max_length=1500)),
                ('createddate', models.DateTimeField(blank=True, db_column='CreatedDate', null=True)),
                ('openedby', models.CharField(blank=True, db_column='OpenedBy', max_length=20, null=True)),
                ('openeddate', models.DateTimeField(blank=True, db_column='OpenedDate', null=True)),
                ('closedby', models.CharField(blank=True, db_column='ClosedBy', max_length=20, null=True)),
                ('closeddate', models.DateTimeField(blank=True, db_column='ClosedDate', null=True)),
                ('canceledby', models.CharField(blank=True, db_column='CanceledBy', max_length=20, null=True)),
                ('canceleddate', models.DateTimeField(blank=True, db_column='CanceledDate', null=True)),
                ('deleted', models.IntegerField(blank=True, db_column='Deleted', null=True)),
            ],
            options={
                'db_table': 'project',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=20)),
                ('name_ar', models.CharField(db_column='Name_Ar', max_length=10)),
                ('priority', models.IntegerField(db_column='Priority')),
                ('isdefault', models.IntegerField(db_column='IsDefault')),
                ('color', models.CharField(db_column='Color', max_length=10)),
            ],
            options={
                'db_table': 'project_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('empid', models.BigIntegerField(blank=True, db_column='EmpId', null=True)),
                ('deptcode', models.IntegerField(blank=True, db_column='DeptCode', null=True)),
                ('managercode', models.BigIntegerField(blank=True, db_column='ManagerCode', null=True)),
                ('managerlevel2', models.BigIntegerField(blank=True, db_column='ManagerLevel2', null=True)),
                ('managerlevel3', models.BigIntegerField(blank=True, db_column='ManagerLevel3', null=True)),
                ('managerlevel4', models.BigIntegerField(blank=True, db_column='ManagerLevel4', null=True)),
                ('taskdesc', models.CharField(blank=True, db_column='TaskDesc', max_length=255, null=True, verbose_name='Task Descreption')),
                ('tasktype', models.CharField(blank=True, choices=[('', 'Choice type'), ('m', 'Master'), ('h', 'Help')], db_column='TaskType', max_length=1, null=True, verbose_name='Task type')),
                ('duration', models.IntegerField(blank=True, db_column='Duration', null=True, verbose_name='Duration')),
                ('createddate', models.DateTimeField(blank=True, db_column='CreatedDate', null=True)),
                ('taskdate', models.DateField(db_column='TaskDate', verbose_name='task date')),
                ('editedate', models.DateTimeField(blank=True, db_column='EditeDate', null=True)),
                ('ifsubmitted', models.CharField(blank=True, choices=[('', 'Choice action'), ('0', 'New'), ('1', 'submitted'), ('2', 'not submitted')], db_column='IfSubmitted', max_length=1, null=True)),
                ('status', models.CharField(choices=[('', 'Choice status'), ('0', 'New'), ('1', 'in progres'), ('2', 'Done'), ('3', 'Ignore')], db_column='Status', max_length=1)),
                ('statusdate', models.DateTimeField(blank=True, db_column='StatusDate', null=True)),
                ('reason', models.CharField(blank=True, choices=[('', 'Choice reason'), ('0', 'Need Support'), ('1', 'Change piroty')], db_column='Reason', max_length=1, null=True)),
                ('submittedby', models.IntegerField(blank=True, db_column='SubmittedBy', null=True)),
                ('submitteddate', models.DateTimeField(blank=True, db_column='SubmittedDate', null=True)),
            ],
            options={
                'db_table': 'sheet',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=200)),
                ('desc', models.CharField(db_column='Desc', max_length=2500)),
                ('status', models.CharField(choices=[('', 'Choice action'), ('New', 'New'), ('InProgress', 'InProgress'), ('Done', 'Done'), ('Hold', 'Hold'), ('Cancelled', 'Cancelled'), ('Closed', 'Closed')], db_column='Status', max_length=10)),
                ('startdate', models.DateTimeField(blank=True, db_column='StartDate', null=True)),
                ('enddate', models.DateTimeField(blank=True, db_column='EndDate', null=True)),
                ('assigneddate', models.DateTimeField(blank=True, db_column='AssignedDate', null=True)),
                ('progress', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('realstartdate', models.DateTimeField(blank=True, db_column='RealStartDate', null=True)),
                ('realstartby', models.IntegerField(blank=True, db_column='RealStartBy', null=True)),
                ('finishedby', models.IntegerField(blank=True, db_column='FinishedBy', null=True)),
                ('finisheddate', models.DateTimeField(blank=True, db_column='FinishedDate', null=True)),
                ('cancelledby', models.IntegerField(blank=True, db_column='CancelledBy', null=True)),
                ('cancelleddate', models.DateTimeField(blank=True, db_column='CancelledDate', null=True)),
                ('closedby', models.IntegerField(blank=True, db_column='ClosedBy', null=True)),
                ('closeddate', models.DateTimeField(blank=True, db_column='ClosedDate', null=True)),
                ('closereson', models.CharField(blank=True, db_column='CloseReson', max_length=500, null=True)),
                ('deleted', models.IntegerField(blank=True, db_column='Deleted', null=True)),
                ('createddate', models.DateTimeField(blank=True, db_column='CreatedDate', null=True)),
                ('lasteditdate', models.DateTimeField(blank=True, db_column='LastEditDate', null=True)),
            ],
            options={
                'db_table': 'task',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaskHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectid', models.IntegerField(db_column='ProjectId')),
                ('taskid', models.IntegerField(db_column='TaskId')),
                ('actionname', models.IntegerField(db_column='ActionName')),
                ('actiondate', models.IntegerField(db_column='ActionDate')),
                ('notes', models.IntegerField(db_column='Notes')),
            ],
            options={
                'db_table': 'task_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=20)),
                ('name_ar', models.CharField(db_column='Name_Ar', max_length=20)),
            ],
            options={
                'db_table': 'task_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VDeptsheetsdata',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('deptcode', models.IntegerField(blank=True, db_column='DeptCode', null=True)),
                ('deptname', models.CharField(blank=True, db_column='DeptName', max_length=200, null=True)),
                ('mangerid', models.CharField(blank=True, db_column='MangerID', max_length=45, null=True)),
                ('empname', models.CharField(blank=True, db_column='EmpName', max_length=255, null=True)),
                ('totaltask', models.BigIntegerField(db_column='TotalTask')),
                ('done', models.BigIntegerField(blank=True, db_column='Done', null=True)),
                ('inprogress', models.BigIntegerField(blank=True, db_column='INPROGRESS', null=True)),
                ('notcomplete', models.BigIntegerField(blank=True, db_column='NOTCOMPLETE', null=True)),
                ('new', models.BigIntegerField(blank=True, db_column='NEW', null=True)),
            ],
            options={
                'db_table': 'v_deptsheetsdata',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VFollowup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(blank=True, db_column='taskName', max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('assignedto', models.IntegerField(blank=True, db_column='AssignedTo', null=True)),
                ('projectid', models.IntegerField(blank=True, db_column='projectId', null=True)),
                ('projectname', models.CharField(blank=True, db_column='projectName', max_length=250, null=True)),
                ('empname', models.CharField(blank=True, db_column='EmpName', max_length=255, null=True)),
                ('deptcode', models.CharField(blank=True, db_column='DeptCode', max_length=45, null=True)),
                ('deptname', models.CharField(blank=True, db_column='DeptName', max_length=200, null=True)),
            ],
            options={
                'db_table': 'v_followup',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VSheetsdata',
            fields=[
                ('id', models.IntegerField(db_column='Id', primary_key=True, serialize=False)),
                ('employeeid', models.CharField(blank=True, db_column='EmployeeId', max_length=45, null=True)),
                ('employeename', models.CharField(blank=True, db_column='EmployeeName', max_length=255, null=True)),
                ('deptname', models.CharField(blank=True, db_column='DeptName', max_length=200, null=True)),
                ('deptcode', models.CharField(blank=True, db_column='DeptCode', max_length=45, null=True)),
                ('managername', models.CharField(blank=True, db_column='ManagerName', max_length=255, null=True)),
                ('totaltask', models.BigIntegerField(db_column='TotalTask')),
                ('notsubmitted', models.BigIntegerField(blank=True, db_column='NotSubmitted', null=True)),
                ('submitted', models.BigIntegerField(blank=True, db_column='Submitted', null=True)),
                ('new', models.BigIntegerField(blank=True, db_column='New', null=True)),
            ],
            options={
                'db_table': 'V_SheetsData',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VStatisticstaskdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectid', models.IntegerField(db_column='ProjectId')),
                ('proid', models.IntegerField(db_column='proID')),
                ('employeeid', models.CharField(blank=True, db_column='EmployeeId', max_length=45, null=True)),
                ('employeename', models.CharField(blank=True, db_column='EmployeeName', max_length=255, null=True)),
                ('jobtitle', models.CharField(blank=True, db_column='JobTitle', max_length=200, null=True)),
                ('deptname', models.CharField(blank=True, db_column='DeptName', max_length=200, null=True)),
                ('deptcode', models.CharField(blank=True, db_column='DeptCode', max_length=45, null=True)),
                ('managername', models.CharField(blank=True, db_column='ManagerName', max_length=255, null=True)),
                ('totaltask', models.BigIntegerField(blank=True, db_column='TotalTask', null=True)),
                ('new', models.BigIntegerField(blank=True, db_column='New', null=True)),
                ('inprogress', models.BigIntegerField(blank=True, db_column='Inprogress', null=True)),
                ('done', models.BigIntegerField(blank=True, db_column='Done', null=True)),
                ('closed', models.BigIntegerField(blank=True, db_column='Closed', null=True)),
                ('cancelled', models.BigIntegerField(blank=True, db_column='Cancelled', null=True)),
            ],
            options={
                'db_table': 'v_statisticstaskdata',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalTask',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=200)),
                ('desc', models.CharField(db_column='Desc', max_length=2500)),
                ('status', models.CharField(choices=[('', 'Choice action'), ('New', 'New'), ('InProgress', 'InProgress'), ('Done', 'Done'), ('Hold', 'Hold'), ('Cancelled', 'Cancelled'), ('Closed', 'Closed')], db_column='Status', max_length=10)),
                ('startdate', models.DateTimeField(blank=True, db_column='StartDate', null=True)),
                ('enddate', models.DateTimeField(blank=True, db_column='EndDate', null=True)),
                ('assigneddate', models.DateTimeField(blank=True, db_column='AssignedDate', null=True)),
                ('progress', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('realstartdate', models.DateTimeField(blank=True, db_column='RealStartDate', null=True)),
                ('realstartby', models.IntegerField(blank=True, db_column='RealStartBy', null=True)),
                ('finishedby', models.IntegerField(blank=True, db_column='FinishedBy', null=True)),
                ('finisheddate', models.DateTimeField(blank=True, db_column='FinishedDate', null=True)),
                ('cancelledby', models.IntegerField(blank=True, db_column='CancelledBy', null=True)),
                ('cancelleddate', models.DateTimeField(blank=True, db_column='CancelledDate', null=True)),
                ('closedby', models.IntegerField(blank=True, db_column='ClosedBy', null=True)),
                ('closeddate', models.DateTimeField(blank=True, db_column='ClosedDate', null=True)),
                ('closereson', models.CharField(blank=True, db_column='CloseReson', max_length=500, null=True)),
                ('deleted', models.IntegerField(blank=True, db_column='Deleted', null=True)),
                ('createddate', models.DateTimeField(blank=True, db_column='CreatedDate', null=True)),
                ('lasteditdate', models.DateTimeField(blank=True, db_column='LastEditDate', null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('assignedto', models.ForeignKey(blank=True, db_column='assignedto', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='project.Employee', to_field='empid')),
                ('createdby', models.ForeignKey(blank=True, db_column='CreatedBy', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='project.Employee', to_field='empid')),
                ('departement', models.ForeignKey(blank=True, db_column='departementid', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='project.Department', to_field='deptcode')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('lasteditby', models.ForeignKey(blank=True, db_column='LastEditBy', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='project.Employee', to_field='empid')),
                ('project', models.ForeignKey(blank=True, db_column='projectid', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='project.Project')),
            ],
            options={
                'verbose_name': 'historical task',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('filename', models.CharField(blank=True, max_length=100, null=True)),
                ('filepath', models.FileField(blank=True, null=True, upload_to='documents/', verbose_name='Files Upload')),
                ('project', models.ForeignKey(blank=True, db_column='projectid', null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.Project')),
                ('task', models.ForeignKey(blank=True, db_column='taskid', null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.Task')),
            ],
            options={
                'db_table': 'media',
            },
        ),
    ]
