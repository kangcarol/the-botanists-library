# Generated by Django 4.1.3 on 2022-11-08 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flower',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='garden',
            options={'ordering': ['name']},
        ),
    ]