# Generated by Django 3.2.10 on 2021-12-19 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20211219_0737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
    ]
