# Generated by Django 5.1.6 on 2025-02-26 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='cantidad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
