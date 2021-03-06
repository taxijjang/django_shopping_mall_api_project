# Generated by Django 3.2.10 on 2022-02-15 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0002_alter_purchase_tid'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseApprovalResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('aid', models.CharField(max_length=50, verbose_name='요청 고유 변호')),
                ('payment_type', models.CharField(max_length=5, verbose_name='결제 수단')),
                ('total_amount', models.IntegerField(verbose_name='결제총액')),
                ('tax_free_amount', models.IntegerField(verbose_name='상품 비과세 금액')),
                ('vat_amount', models.IntegerField(default=0, verbose_name='상품 부가세 금액')),
                ('card_info', models.TextField(blank=True, null=True)),
                ('item_name', models.CharField(max_length=100)),
                ('ready_at', models.DateTimeField()),
                ('approved_at', models.DateTimeField()),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='purchases.purchase', verbose_name='주문번호')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
