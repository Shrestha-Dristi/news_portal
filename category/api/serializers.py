from category.models import Category
from rest_framework import serializers
from user.api.serializers import UserInfoSerializer

class CatSerializers(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    test = serializers.CharField(required=False,allow_null=True, allow_blank=False)

    class Meta:
        model = Category
        fields = '__all__'
