# Generated by Django 3.2.10 on 2022-02-15 15:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0005_remove_purchase_finish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='purchaseapprovalresult',
            name='payment_type',
            field=models.CharField(db_index=True, max_length=5, verbose_name='결제 수단'),
        ),
    ]
