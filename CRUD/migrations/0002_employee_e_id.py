# Generated by Django 4.1.7 on 2023-03-15 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='e_id',
            field=models.CharField(default='NA', max_length=10),
        ),
    ]