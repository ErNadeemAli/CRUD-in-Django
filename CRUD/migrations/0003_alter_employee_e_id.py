# Generated by Django 4.1.7 on 2023-03-15 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0002_employee_e_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='e_id',
            field=models.CharField(default='', max_length=10),
        ),
    ]
