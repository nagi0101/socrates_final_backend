from rest_framework import serializers

from reviews.models import Review, Tag

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    tags=TagSerializer(many=True, required=False)
    place_id=serializers.IntegerField()
    
    class Meta:
        model=Review
        fields='__all__'
    
    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        instance = Review.objects.create(**validated_data)
        for tag in tags:
            tag_instance, _ = Tag.objects.get_or_create(name=tag["name"])
            instance.tags.add(tag_instance)
        return instance
    
    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])

        instance = super().update(instance, validated_data)

        instance.tags.clear()

        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
            instance.tags.add(tag)

        return instance
