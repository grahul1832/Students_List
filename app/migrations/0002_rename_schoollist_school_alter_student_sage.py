# Generated by Django 4.2.3 on 2023-08-08 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SchoolList',
            new_name='School',
        ),
        migrations.AlterField(
            model_name='student',
            name='sage',
            field=models.IntegerField(),
        ),
    ]