# Generated by Django 3.2.14 on 2022-07-05 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0010_auto_20220705_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacientes',
            name='photocopy_document',
            field=models.FileField(default=False, upload_to=''),
        ),
    ]
