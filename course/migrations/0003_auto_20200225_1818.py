# Generated by Django 3.0.3 on 2020-02-26 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20200225_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='TCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Docente', models.CharField(max_length=200)),
                ('Hora', models.CharField(max_length=200)),
                ('Fecha', models.CharField(max_length=200)),
                ('Aula', models.CharField(max_length=200)),
                ('Ingenieria', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]