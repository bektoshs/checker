# Generated by Django 4.0.10 on 2024-07-22 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteWithIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(db_index=True, max_length=255, unique=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
