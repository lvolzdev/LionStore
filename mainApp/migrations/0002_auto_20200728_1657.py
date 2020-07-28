# Generated by Django 3.0.8 on 2020-07-28 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mainApp.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodPoint', models.TextField(verbose_name='장점')),
                ('weakPoint', models.TextField(verbose_name='단점')),
                ('reported', models.BooleanField(default=False, verbose_name='신고')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewAuthor', to=settings.AUTH_USER_MODEL, verbose_name='리뷰 작성자')),
                ('likers', models.ManyToManyField(related_name='reviewLikers', to=settings.AUTH_USER_MODEL, verbose_name='좋아요')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewTargetProduct', to='mainApp.Product', verbose_name='대상 상품')),
            ],
        ),
        migrations.CreateModel(
            name='WebSellInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=300, verbose_name='판매정보 링크')),
                ('price', models.PositiveIntegerField(verbose_name='판매가')),
                ('reported', models.BooleanField(default=False, verbose_name='신고')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='webSellInfoTargetProduct', to='mainApp.Product', verbose_name='대상 상품')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='webSellInfoSeller', to=settings.AUTH_USER_MODEL, verbose_name='웹 판매자')),
            ],
        ),
        migrations.CreateModel(
            name='StationerSellInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(verbose_name='판매가')),
                ('reported', models.BooleanField(default=False, verbose_name='신고')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StationerSellInfoTargetProduct', to='mainApp.Product', verbose_name='대상 상품')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='StationerSellInfoSeller', to=settings.AUTH_USER_MODEL, verbose_name='문방구 판매자')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='평가 항목')),
                ('score', mainApp.models.RangedScoreField(verbose_name='평가 점수')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scoreTargetReview', to='mainApp.Review', verbose_name='대상 리뷰')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewImage', models.ImageField(blank=True, null=True, upload_to='review_image/', verbose_name='리뷰 이미지')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewImageTargetReview', to='mainApp.Review', verbose_name='대상 리뷰')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='totalScore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewTotalScore', to='mainApp.Score', verbose_name='총점'),
        ),
        migrations.CreateModel(
            name='ProductVideoLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoLink', models.CharField(max_length=100, verbose_name='유튜브 링크')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linkTargetProduct', to='mainApp.Product', verbose_name='대상 상품')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=15, verbose_name='상품 태그')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagTargetReview', to='mainApp.Review', verbose_name='대상 리뷰')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productImage', models.ImageField(upload_to='product_image/', verbose_name='상품 이미지')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imageTargetProduct', to='mainApp.Product', verbose_name='대상 상품')),
            ],
        ),
        migrations.CreateModel(
            name='PenReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costEffetiveness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='costEffetiveness', to='mainApp.Score', verbose_name='가성비')),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='design', to='mainApp.Score', verbose_name='디자인')),
                ('durability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='durability', to='mainApp.Score', verbose_name='내구도')),
                ('grip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grip', to='mainApp.Score', verbose_name='그립감')),
                ('life', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='life', to='mainApp.Score', verbose_name='제품 수명')),
                ('texture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='texture', to='mainApp.Score', verbose_name='사용감')),
                ('versatility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versatility', to='mainApp.Score', verbose_name='범용성')),
            ],
        ),
    ]
