# Generated by Django 4.1.7 on 2024-10-31 07:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_deposite_date_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposite',
            name='date_created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='expire_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]