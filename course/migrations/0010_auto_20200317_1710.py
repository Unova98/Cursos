# Generated by Django 3.0.3 on 2020-03-17 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_auto_20200317_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursosv2',
            old_name='NumCursos',
            new_name='IdCursos',
        ),
    ]
