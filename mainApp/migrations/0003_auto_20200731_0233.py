# Generated by Django 3.0.8 on 2020-07-30 17:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20200731_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penreview',
            name='costEffetiveness',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='costEffetiveness', to='mainApp.Score', verbose_name='가성비'),
        ),
        migrations.AlterField(
            model_name='penreview',
            name='design',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='design', to='mainApp.Score', verbose_name='디자인'),
        ),
        migrations.AlterField(
            model_name='penreview',
            name='durability',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='durability', to='mainApp.Score', verbose_name='내구도'),
        ),
        migrations.AlterField(
            model_name='penreview',
            name='grip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grip', to='mainApp.Score', verbose_name='그립감'),
        ),
        migrations.AlterField(
            model_name='penreview',
            name='life',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='life', to='mainApp.Score', verbose_name='제품 수명'),
        ),
        migrations.AlterField(
            model_name='penreview',
            name='texture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='texture', to='mainApp.Score', verbose_name='사용감'),
        ),
        migrations.AlterField(
            model_name='penreview',
            name='versatility',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='versatility', to='mainApp.Score', verbose_name='범용성'),
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewTargetProduct', to='mainApp.Product', verbose_name='대상 상품'),
        ),
        migrations.AlterField(
            model_name='review',
            name='totalScore',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewTotalScore', to='mainApp.Score', verbose_name='총점'),
        ),
        migrations.AlterField(
            model_name='score',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scoreTargetReview', to='mainApp.Review', verbose_name='대상 리뷰'),
        ),
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='평가 점수'),
        ),
    ]
