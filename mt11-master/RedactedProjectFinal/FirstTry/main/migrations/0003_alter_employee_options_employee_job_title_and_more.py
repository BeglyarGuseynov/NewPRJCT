# Generated by Django 4.2.2 on 2023-07-01 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_employee_first_name_alter_employee_last_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Сотрудники кафедры', 'verbose_name_plural': 'Сотрудники кафедры'},
        ),
        migrations.AddField(
            model_name='employee',
            name='Job_title',
            field=models.CharField(default='', max_length=50, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(default='', max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(default='', max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mail',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='patronymic',
            field=models.CharField(default='', max_length=50, verbose_name='Отчество'),
        ),
    ]
