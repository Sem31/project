# Generated by Django 2.2.4 on 2019-11-17 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=20)),
                ('MobileNo', models.CharField(max_length=10)),
                ('EmailId', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('ConfirmPassword', models.CharField(max_length=50)),
            ],
        ),
    ]
