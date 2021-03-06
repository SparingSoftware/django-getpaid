# Generated by Django 3.0.6 on 2020-07-17 11:34

from django.db import migrations, models
import django_fsm
import getpaid.types


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200610_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomPayout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backend', models.CharField(db_index=True, max_length=100, verbose_name='backend')),
                ('shop_id', models.CharField(db_index=True, max_length=128)),
                ('customer_name', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=128)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='amount requested')),
                ('ext_customer_id', models.CharField(blank=True, db_index=True, max_length=128)),
                ('currency_code', models.CharField(default='PLN', max_length=128)),
                ('external_id', models.CharField(blank=True, db_index=True, max_length=128, verbose_name='status')),
                ('status', django_fsm.FSMField(choices=[('new', 'new'), ('failed', 'failed'), ('success', 'success')], db_index=True, default=getpaid.types.PayoutStatus['NEW'], max_length=50, protected=True, verbose_name='status')),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created on')),
                ('failed_code', models.CharField(blank=True, max_length=128, verbose_name='Reason of failure')),
                ('custom', models.BooleanField(default=True, editable=False)),
            ],
            options={
                'swappable': 'GETPAID_PAYOUT_MODEL',
            },
        ),
        migrations.AlterModelOptions(
            name='custompayment',
            options={},
        ),
    ]
