# Generated by Django 4.1 on 2022-10-12 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LibCatalogo', '0015_libros_portada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libros',
            name='portada',
        ),
    ]
