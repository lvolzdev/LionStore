# Generated by Django 3.0.8 on 2020-07-28 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='penInterest_1',
            field=models.CharField(choices=[('P1', '형광펜'), ('P2', '유성펜'), ('P3', '볼펜'), ('P4', '샤프펜슬'), ('P5', '기타')], default=('P5', '기타'), max_length=10),
        ),
        migrations.AddField(
            model_name='customer',
            name='penInterest_2',
            field=models.CharField(choices=[('P1', '형광펜'), ('P2', '유성펜'), ('P3', '볼펜'), ('P4', '샤프펜슬'), ('P5', '기타')], default=('P5', '기타'), max_length=10),
        ),
        migrations.AddField(
            model_name='customer',
            name='penInterest_3',
            field=models.CharField(choices=[('P1', '형광펜'), ('P2', '유성펜'), ('P3', '볼펜'), ('P4', '샤프펜슬'), ('P5', '기타')], default=('P5', '기타'), max_length=10),
        ),
    ]
