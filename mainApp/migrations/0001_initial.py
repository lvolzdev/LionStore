# Generated by Django 3.0.8 on 2020-08-21 11:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='상품 이름')),
                ('manufacturer', models.CharField(max_length=30, verbose_name='제조사')),
                ('description', models.TextField(verbose_name='상품 설명')),
                ('registerDate', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('likeCount', models.PositiveIntegerField(default=0, verbose_name='좋아요 수')),
                ('productImage', models.ImageField(upload_to='product_image/', verbose_name='상품 이미지')),
            ],
            options={
                'verbose_name': '제품',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=15, verbose_name='카테고리 이름')),
            ],
            options={
                'verbose_name': '제품 카테고리',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='리뷰 작성일')),
                ('totalScore', models.DecimalField(decimal_places=1, max_digits=2, null=True, verbose_name='총점')),
                ('comment', models.CharField(default='', max_length=50, verbose_name='한줄평')),
                ('goodPoint', models.TextField(verbose_name='장점')),
                ('weakPoint', models.TextField(verbose_name='단점')),
                ('likeCount', models.PositiveIntegerField(default=0, verbose_name='좋아요 수')),
                ('reported', models.BooleanField(default=False, verbose_name='신고')),
                ('modified', models.BooleanField(default=False, verbose_name='수정')),
                ('reviewImage1', models.ImageField(blank=True, null=True, upload_to='review_image/', verbose_name='리뷰 이미지1')),
                ('reviewImage2', models.ImageField(blank=True, null=True, upload_to='review_image/', verbose_name='리뷰 이미지2')),
                ('reviewImage3', models.ImageField(blank=True, null=True, upload_to='review_image/', verbose_name='리뷰 이미지3')),
                ('reviewImage4', models.ImageField(blank=True, null=True, upload_to='review_image/', verbose_name='리뷰 이미지4')),
                ('reviewImage5', models.ImageField(blank=True, null=True, upload_to='review_image/', verbose_name='리뷰 이미지5')),
                ('reviewImage6', models.ImageField(blank=True, null=True, upload_to='review_image/', verbose_name='리뷰 이미지6')),
                ('rawTagString', models.TextField(blank=True, default='', verbose_name='제품 태그 목록 원본 데이터')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewAuthor', to=settings.AUTH_USER_MODEL, verbose_name='리뷰 작성자')),
                ('likers', models.ManyToManyField(related_name='reviewLikers', to=settings.AUTH_USER_MODEL, verbose_name='좋아요')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewTargetProduct', to='mainApp.Product', verbose_name='대상 상품')),
            ],
            options={
                'verbose_name': '제품 리뷰',
            },
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
            options={
                'verbose_name': '웹 판매 정보',
            },
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
            options={
                'verbose_name': '문방구 판매 정보',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='평가 항목')),
                ('score', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='평가 점수')),
                ('review', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scoreTargetReview', to='mainApp.Review', verbose_name='대상 리뷰')),
            ],
            options={
                'verbose_name': '제품 별점',
            },
        ),
        migrations.CreateModel(
            name='ReviewTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=15, verbose_name='상품 태그')),
                ('targetReview', models.ManyToManyField(blank=True, to='mainApp.Review', verbose_name='가리키는 상품')),
            ],
            options={
                'verbose_name': '리뷰 태그',
            },
        ),
        migrations.AddField(
            model_name='review',
            name='tags',
            field=models.ManyToManyField(blank=True, to='mainApp.ReviewTag'),
        ),
        migrations.CreateModel(
            name='ProductVideoLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoLink', models.CharField(max_length=100, verbose_name='유튜브 링크')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linkTargetProduct', to='mainApp.Product', verbose_name='대상 상품')),
            ],
            options={
                'verbose_name': '상품 관련 유튜브 영상 링크',
            },
        ),
        migrations.CreateModel(
            name='ProductRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=20, verbose_name='제품 이름')),
                ('productBrand', models.CharField(blank=True, max_length=20, null=True, verbose_name='제품 브랜드')),
                ('productDescription', models.TextField(blank=True, null=True, verbose_name='제품 설명')),
                ('isChecked', models.BooleanField(default=False, verbose_name='확인여부')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productRequestAuthor', to=settings.AUTH_USER_MODEL, verbose_name='제품 등록 요청자')),
            ],
            options={
                'verbose_name': '상품 등록 요청',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productCategory', to='mainApp.ProductCategory', verbose_name='소속 카테고리'),
        ),
        migrations.AddField(
            model_name='product',
            name='likers',
            field=models.ManyToManyField(blank=True, related_name='productLikers', to=settings.AUTH_USER_MODEL, verbose_name='좋아요'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='리뷰 작성(수정)일')),
                ('body', models.TextField(verbose_name='댓글 내용')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentAuthor', to=settings.AUTH_USER_MODEL, verbose_name='리뷰 작성자')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentTargetReview', to='mainApp.Review', verbose_name='대상 리뷰')),
            ],
        ),
        migrations.CreateModel(
            name='PenReview',
            fields=[
                ('review_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mainApp.Review')),
                ('costEffetiveness', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='costEffetiveness', to='mainApp.Score', verbose_name='가성비')),
                ('design', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='design', to='mainApp.Score', verbose_name='디자인')),
                ('durability', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='durability', to='mainApp.Score', verbose_name='내구도')),
                ('grip', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grip', to='mainApp.Score', verbose_name='그립감')),
                ('life', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='life', to='mainApp.Score', verbose_name='제품 수명')),
                ('texture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='texture', to='mainApp.Score', verbose_name='사용감')),
            ],
            options={
                'verbose_name': '펜 리뷰',
            },
            bases=('mainApp.review',),
        ),
    ]
