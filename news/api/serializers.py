from rest_framework import serializers
from news.models import Tags

class TagSerializers(serializers.ModelSerializer):
    # name = serializers.CharField(required=True)
    class Meta:
        model = Tags
        fields = '__all__'