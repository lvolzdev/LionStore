# Generated by Django 3.0.8 on 2020-08-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_merge_20200826_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
