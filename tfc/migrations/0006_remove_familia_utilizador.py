# Generated by Django 4.0.6 on 2025-02-20 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tfc', '0005_familia_utilizador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familia',
            name='utilizador',
        ),
    ]
