from rest_framework import serializers
from news.models import Tags, News
from author.api.serializers import AuthorSerializers

class TagSerializers(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    class Meta:
        model = Tags
        fields = '__all__'

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author_detail'] = [AuthorSerializers(i).data for i in instance.author.all()]
        data['tags_detail'] = [TagSerializers(i).data for i in instance.tags.all()]
        data['broadway'] = "This is from to_representation" 
        return data


