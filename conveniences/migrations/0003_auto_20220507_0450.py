# Generated by Django 3.2.10 on 2022-05-07 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conveniences', '0002_alter_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='modified',
            new_name='modified_at',
        ),
    ]
