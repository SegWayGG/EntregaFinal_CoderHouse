# Generated by Django 4.1 on 2022-10-12 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibCatalogo', '0008_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='libros',
            name='portada',
            field=models.ImageField(default=2, upload_to='portadas'),
            preserve_default=False,
        ),
    ]