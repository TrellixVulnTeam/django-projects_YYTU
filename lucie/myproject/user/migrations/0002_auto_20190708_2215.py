# Generated by Django 2.2.3 on 2019-07-08 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('confirm_password', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
