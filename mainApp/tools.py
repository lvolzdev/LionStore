from django.http import HttpResponseRedirect

from faker import Faker
import random

from .models import PenReview, ProductCategory
from account.models import Customer, CustomerTag
from . import views

CATEGORY_NAMES = tuple("볼펜 만년필 캘리그라피펜 연필 색연필 형광펜 샤프펜슬 유성펜 사인펜 젤펜 기타".split(' '))

from mainApp.models import Product, ProductCategory, Review

# CATEGORY_NAMES에 있는 카테고리를 카테고리 목록이 비었을 때만 자동으로 생성해줌
def initializeCategory():
    # 카테고리 리스트가 비었을 때만 사용하기
    if len(ProductCategory.objects.all()) != 0:
        return
    
    for name in CATEGORY_NAMES:
        ProductCategory.objects.create(categoryName=name)


# 자동으로 countLimit개의 상품을 만들고 카테고리에 매칭해줌
def automativeFilling_Product(countLimit=10):
    fakerInstance = Faker()

    productList = Product.objects.all()

    if len(productList) > countLimit:
        print(f"이미 {countLimit}개의 Product 모델이 존재해 새로 모델을 생성하지 않습니다.")
        return

    categories = ProductCategory.objects.all()
    for i in range(countLimit - len(productList)):
        Product.objects.create(category=random.choice(categories), manufacturer=fakerInstance.name(), description=fakerInstance.text(), name=fakerInstance.name())


# 유튜브 링크로부터 해쉬값을 뽑아옴
def getHash(rawLink):
    return rawLink.split('/')[-1]


# 리뷰에 이미지를 하나도 등록하지 않았는지 확인
def hasImageField(instance:Review):
    imageFields = [
        instance.reviewImage1, instance.reviewImage2, instance.reviewImage3,
        instance.reviewImage4, instance.reviewImage5, instance.reviewImage6
    ]

    return len(list(filter(lambda x : x, imageFields))) != 0


def likeProcess_RandomReviews(request, num=10):
    if not request.user.is_authenticated:
        return
    
    reviews = PenReview.objects.all()
    for _ in range(num):
        views.reviewLikeProcess(request, random.choice(reviews).id)


def likeProcess_RandomProducts(request, num=10):
    if not request.user.is_authenticated:
        return
    
    products = Product.objects.all()
    for _ in range(num):
        views.productLikeProcess(request, random.choice(products).id)


def redirectExternalLink(request, link):
    return HttpResponseRedirect(link)


def getCategoryId(categoryName):
    return ProductCategory.objects.get(categoryName=categoryName).id

def redirectByCategoryName(request, categoryName):
    id = getCategoryId(categoryName)
    return views.productList_view(request, id)

def getReviewerTagTooltip(user : Customer):
    if user.is_Stationer:
        return "문구점 사장님입니다."
    elif user.is_WebSeller:
        return "웹 판매자입니다."

    user_usage = ("주 사용 용도", user.usage, Customer.usage_dict[user.usage])
    user_job = ("직업", user.job, Customer.job_dict[user.job])
    user_age = ("연령", user.age, Customer.age_dict[user.age])
    userPropertyList = list(filter(lambda choice: choice[-1] != "기타", [user_usage, user_job, user_age]))

    if len(userPropertyList) <= 0 :
        return "모든 정보가 비공개 되어 있습니다."
    
    else :
        return " | ".join([f"{p[-1]}" for p in userPropertyList])