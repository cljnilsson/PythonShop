# Generated by Django 3.1.3 on 2020-12-15 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200515_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='product',
            name='specifications',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
