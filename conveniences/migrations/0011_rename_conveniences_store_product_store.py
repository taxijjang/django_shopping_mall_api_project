# Generated by Django 3.2.10 on 2022-05-08 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conveniences', '0010_auto_20220508_1526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='conveniences_store',
            new_name='store',
        ),
    ]