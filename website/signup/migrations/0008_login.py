# Generated by Django 2.2.7 on 2019-11-26 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0007_remove_signup_confirm_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('pasword', models.CharField(max_length=50)),
            ],
        ),
    ]
