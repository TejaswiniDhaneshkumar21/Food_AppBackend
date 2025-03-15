# Generated by Django 5.1.6 on 2025-02-27 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('genus', models.CharField(blank=True, max_length=100)),
                ('family', models.CharField(blank=True, max_length=100)),
                ('order', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
