# Generated by Django 5.1.5 on 2025-03-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_studentapplication_academic_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentapplication',
            name='fee_balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]
