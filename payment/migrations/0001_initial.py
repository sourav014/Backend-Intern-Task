# Generated by Django 4.1.5 on 2023-01-27 04:49

from django.db import migrations, models
import payment.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=256)),
                ('order_amount', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('order_status', models.CharField(choices=[('SUCCESS', 'SUCCESS'), ('FAILURE', 'FAILURE'), ('NO_RESPONSE', 'NO_RESPONSE')], default='NO_RESPONSE', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('metadata', models.JSONField(blank=True, default=dict, encoder=payment.models.CustomJsonEncoder, null=True)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]