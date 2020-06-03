from rest_framework import serializers, fields

from .models import Company, Ingredient, Product, Category
from users.models import INFLUENCER_CHOICES, SKINISSUE_CHOICES, SKINTYPE_CHOICES


class ProductSerializer(serializers.ModelSerializer):

    skintype = fields.MultipleChoiceField(choices=SKINTYPE_CHOICES, default = 'C')
    skinissue = fields.MultipleChoiceField(choices=SKINISSUE_CHOICES, default = 'N/A')
    reviews = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'photo', 'description', 'company', 'category',
                  'skintype', 'skinissue', 'ingredients', 
                  'reviews', 'average_star', 'star_number', 'star_sum', 'profile']


class CompanySerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True)

    class Meta:
        model = Company
        fields = ['name', 'year', 'description', 'products']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']


class CategorySerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ['name', 'products']
