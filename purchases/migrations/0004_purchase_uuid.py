# Generated by Django 3.2.10 on 2022-02-15 15:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0003_purchaseapprovalresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
