from rest_framework import serializers
from .models import Products,ProductCategory

# By default, Django will serialize the ForeignKey field as the related object ID 
# (in this case, probably the primary key of the ProductCategory instance) 
# rather than the actual category name.

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['category_id','category_name']
        read_only_fields = ['category_id']

class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(write_only=True)
    # category_name = serializers.SerializerMethodField()

    class Meta:
        model = Products
        exclude = ['created_at','updated_at']

    def get_category_name(self,obj):
        return obj.category.category_name

    # def validate_category(self, value):
    #     if not ProductCategory.objects.filter(category_id=value).exists():
    #         raise serializers.ValidationError("The specified category does not exist.")
    #     return value

    # def create(self, validated_data):
    #     category_name = validated_data.pop('category')  
    #     category = ProductCategory.objects.get(category_id=category_name)  
    #     validated_data['category'] = category  
    #     return Products.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     if 'category' in validated_data:
    #         category_name = validated_data.pop('category')
    #         category = ProductCategory.objects.get(category_id=category_name)
    #         instance.category_name = category
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #     instance.save()
    #     return instance