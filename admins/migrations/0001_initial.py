# Generated by Django 5.1.5 on 2025-03-17 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_open', models.BooleanField(default=False)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('academic_year', models.CharField(max_length=9, unique=True)),
            ],
        ),
    ]
