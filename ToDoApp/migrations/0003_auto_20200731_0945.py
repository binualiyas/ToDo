# Generated by Django 3.0.8 on 2020-07-31 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0002_auto_20200730_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.CharField(max_length=60),
        ),
    ]
