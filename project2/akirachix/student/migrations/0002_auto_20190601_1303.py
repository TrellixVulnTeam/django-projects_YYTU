# Generated by Django 2.2.1 on 2019-06-01 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id_name',
            field=models.IntegerField(),
        ),
    ]